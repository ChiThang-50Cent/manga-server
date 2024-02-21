from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, style={'input_type': 'password'}, required=True)

    def validate(self, attrs):
        email = attrs['email'].lower()
        password = attrs['password']

        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email is not exists")

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        # user = True

        if not user:
            raise serializers.ValidationError("Email or password is wrong")
        
        attrs['user'] = user

        return attrs

class CreateUserSerializer(serializers.ModelSerializer):
    
    password_2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

        extra_kwargs = {
            'password' : {'required' : True},
            'password_2' : {'required' : True}
        }
    
    def validate(self, attrs):
        email = attrs['email'].strip().lower()
        
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email has been used.")
        
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError("Password must be matched")
        
        return attrs
    
    def create(self, validated_data):
        
        validated_data.pop('password_2', None)
        user = CustomUser.objects.create_user(**validated_data)

        return user