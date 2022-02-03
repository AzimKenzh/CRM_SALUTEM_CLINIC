from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, password, status):
        username = self.normalize_username(username)
        user = self.model(username=username, status=status)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None):
        username = self.normalize_username(username)
        user = self.model(username=username)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, verbose_name='Почта', null=True)
    is_active = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = 'Пользователи'

