

# Django
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self,**kwages) -> (object):
        user = self.model(
            userName=kwages['userName'],
            nickName=kwages['nickName'],
            email=kwages['email']
        )
        user.set_password(kwages['password'])
        user.save(using=self._db)
        return user


    def create_superuser(self,**kwages) -> (object):
        superuser = self.create_user(**kwages)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser , PermissionsMixin):

    objects = CustomUserManager()

    imageProfile = models.ImageField(upload_to='img/profiles/')
    userName = models.CharField(max_length=20,blank=False,null=False,help_text='Nombre de usuario')
    nickName = models.CharField(max_length=50,unique=True,null=False,blank=False)
    email = models.EmailField(unique=True,null=False,blank=False)
    description = models.CharField(max_length=100,blank=True,default='')
    pagePersonal = models.URLField(blank=True)

    is_acces = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_check = models.BooleanField(default=False)

    date_created = models.DateField(auto_now_add=True)


    USERNAME_FIELD = 'nickName'
    REQUIRED_FIELDS = [ 'userName','email' ]

    def __str__(self) -> (str):
        return self.nickName
