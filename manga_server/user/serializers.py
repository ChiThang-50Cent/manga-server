from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(
        max_length=128, 
        required=True, 
        write_only=True, 
        validators=[validate_password]
    )

    password_2 = serializers.CharField(max_length=128, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "password_2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_2"]:
            raise serializers.ValidationError("Not matching password")

        return attrs

    def create(self, validated_data):
        user = CustomUser()

        user.email = validated_data["email"]
        user.set_password(validated_data["password"])

        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
