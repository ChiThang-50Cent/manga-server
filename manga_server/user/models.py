from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_viewer = True
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_viewer', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_uploader', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('SU must have all perms')
        
        if not extra_fields.get('is_uploader'):
            raise ValueError('SU must have all perms')

        if not extra_fields.get('is_superuser'):
            raise ValueError('SU must have all perms')
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=31, null=True, blank=True)
    last_name = models.CharField(max_length=31, null=True, blank=True)
    
    is_viewer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_uploader = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True