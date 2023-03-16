from rest_framework import serializers
from django.contrib.auth import password_validation
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # Hide password from displaying
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # Add mobile number limit
    mobile = serializers.IntegerField(max_value=9999999999, min_value=1000000000)

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'mobile', 'address', 'email', 'password']

    # Set Validation for Password
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

