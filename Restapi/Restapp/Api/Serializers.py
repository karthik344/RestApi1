from rest_framework import serializers
from Restapp.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields =['user']

    #validating serializers at field level

    def validate_content(self,value):
        if len(value)>1000:
            raise serializers.ValidationError("this is too long characters")
        return value

    #validating total data

    def validate(self,data):
        content =data.get("content",None)
        if content == "":
            content = None
        image =data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is needed")
        return data

    from rest_framework import serializers
    class CustomSerializer(serializers.Serializer):
        content = serializers.CharField()
        email = serializers.EmailField()

    #data ={'email':'hello@gmail.com','content':'please delete me'}
    #create_obj_serializer = CustomSerializer(data=data)
    #if create_obj_serializer.is_valid():
     # valid_data = create_obj_serializer.data
    #print(valid_data)

