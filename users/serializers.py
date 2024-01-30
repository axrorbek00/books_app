from rest_framework import serializers
from .models import UserModel
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator])
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_fields = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):  # barcha validlardan song 1 - bolib create iwlaydi
        user = UserModel.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_image', 'first_name', 'last_name', 'email',  'birthday', 'address',
                  'work_address', 'phone', 'profile_id', 'gender']
