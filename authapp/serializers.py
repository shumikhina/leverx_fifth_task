from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from authapp.models import User


class RegisterUserSerializer(serializers.Serializer):

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[(1, 'student'), (2, 'professor')], write_only=True)
    token = serializers.CharField(read_only=True)

    @staticmethod
    def _validate_passwords(password, confirm_password):
        return password == confirm_password

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if username and password and confirm_password:
            if self._validate_passwords(password, confirm_password):
                return attrs
            else:
                return ValidationError('Passwords do not match')
        else:
            return ValidationError('You have to provide username and password twice')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user
