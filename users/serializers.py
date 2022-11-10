from dataclasses import fields
from rest_framework import serializers
from users.models import User,UserManager
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) #해싱해주기위함
        user.save() #db에 전달
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) #해싱해주기위함
        user.save() #db에 전달
        return user

    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['token_message'] = "sparta_time_attack"
        return token