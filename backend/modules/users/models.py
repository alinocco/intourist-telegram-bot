from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from modules.users.managers import UserManager
from modules.utils.models import BaseModel


class User(AbstractUser, BaseModel):
    """
    Custom user model where email is a unique identifier instead of username.
    """
    username = models.CharField(verbose_name="Username", max_length=150, blank=True)
    email = models.EmailField(verbose_name="Email", unique=True)

    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True)
    phone = PhoneNumberField(verbose_name="Телефон", blank=True, null=True)
    telegram_id = models.IntegerField(verbose_name="Telegram ID", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.email}"

    class Meta:
        _splash = "Пользовател%s"
        verbose_name = _splash % "ь"
        verbose_name_plural = _splash % "и"

    def __str__(self):
        return self.email
