from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions
from django.contrib.auth import authenticate,get_user_model
from rest_framework_jwt.settings import api_settings
from django.db.models import Q
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

user = get_user_model()

class AuthView(APIView):
    #authentication_classes = []
    permission_classes = [permissions.AllowAny]
    def post(self,request,*args,**kwargs):
        #print(request.user)
        if request.user.is_authenticated():
            return Response({'detail':'you already authenticated'},status =400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username,password=password)
        qs = user.objects.filter(
            Q(user__iexact=username),
            Q(email__iexact=username)
        ).distinct()
        if qs.count()==1:
            user_obj =qs.first()
            if user_obj.check_password(password):
               user =user_obj


               payload = jwt_payload_handler(user)
               token = jwt_encode_handler(payload)
               response = jwt_response_payload_handler(token,user,request=request)
               return Response({"detail":"inavlid credentials"},status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]



# class RegsiterAPIView(APIView):
#
#             permission_classes = [permissions.AllowAny]
#
#             def post(self, request, *args, **kwargs):
#
#                 if request.user.is_authenticated():
#                     return Response({'detail': 'you already authenticated'}, status=400)
#                 data = request.data
#                 username = data.get('username')
#                 password = data.get('password')
#                 Email = data.get('username')
#                 password2 = data.get('password2')
#                 qs = User.objects.filter(
#                     Q(user__iexact=username),
#                     Q(email__iexact=username)
#                 )
#                 if password!= password2:
#                     return Response({"password":"password must match"},status =400)
#                 if qs.exists():
#                     return Response({"detail":"this user already exists"},status=400)
#                 else:
#                     user = User.objects.create(username = username,Email = Email)
#                     user.set_password(password)
#                     user.save()
#                     payload = jwt_payload_handler(user)
#                     token = jwt_encode_handler(payload)
#                     response = jwt_response_payload_handler(token, user, request=request)
#                 return Response({"detail": "inavlid Request"}, status=401)