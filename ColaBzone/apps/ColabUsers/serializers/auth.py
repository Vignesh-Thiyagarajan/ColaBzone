from rest_framework import serializers
from ..models import ColabUser, UserType


class ColabSuperUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user_type = UserType.objects.get(user_type="SuperAdmin")
        attrs['user_type'] = user_type
        return attrs

    class Meta:
        model = ColabUser
        fields = ['email', 'password']


class ColabUserSerializer(ColabSuperUserSerializer):
    def validate(self, attrs):
        user_type = UserType.objects.get(user_type="ColabUser")
        attrs['user_type'] = user_type
        return attrs


class ColabUserLoginSerializer(ColabSuperUserSerializer):
    class Meta:
        model = ColabUser
        fields = ['email', 'password']
