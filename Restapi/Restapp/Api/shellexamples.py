from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Restapp.Api.Serializers import StatusSerializer
from Restapp.models import Status



#Serialize a Single object

obj =Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


#swerialize query set


qs = Status.objects.all()
serializer2 = StatusSerializer(qs,  many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)

# create object
data ={'user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()  #if serializer is valid than save the serialize data
serializer.save()


#Update Object

obj = Status.objects.first()
data ={'content':'This is newly updated serialized data',"user":1}
update_serializer = StatusSerializer(obj,data=data)
update_serializer.is_valid()
update_serializer.save()

#creating and deleting objects

data ={'user':1,'content':'please delete me'}
create_obj_serializer = StatusSerializer(data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
print(obj.delete())

