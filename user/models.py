from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = User(
            email=BaseUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email=email,
                             password=password)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False
    )
    password = models.CharField(
        _('password'),
        max_length=128
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def update(self, **kwargs):
        print(self.is_authenticated)
        new_password = kwargs.get('password')
        if new_password is not None:
            del kwargs['password']
            self.set_password(new_password)

        for attr in kwargs.keys():
            setattr(self, attr, kwargs.get(attr))

        self.save()
        return self

    def to_dict(self):
        return {
            "pk": self.pk,
            "email": self.email,
            "is_staff": self.is_staff,
            "is_superuser": self.is_superuser,
            "last_login": self.last_login
        }

    @classmethod
    def to_list(cls, base=None, **kwargs):
        base = cls.objects.all() if base is None else base
        try:
            filtered = base.filter(**kwargs)
        except AttributeError as e:
            print(e)
            filtered = []

        return [user.to_dict() for user in filtered]

    def __repr__(self):
        return "{}. {}".format(self.pk, self.email)

    __str__ = __repr__
