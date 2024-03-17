from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.models import Group, Permission
# Create your models here.

class CustomeUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El E-mail que ha ingresado no es valido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomeUserManager()
    
    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.IntegerField(default = 0)
    availability_xs = models.IntegerField( default=0)
    availability_s = models.IntegerField(default=0)
    availability_m = models.IntegerField(default=0)
    availability_l = models.IntegerField(default=0)
    availability_xl = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.name
    