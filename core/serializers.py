from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserSignUpSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)


class UserSignInSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)
