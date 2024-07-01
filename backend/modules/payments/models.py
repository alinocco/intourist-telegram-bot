from django.db import models

from modules.payments.consts import PAYMENT_CHANNEL_CHOICES
from modules.utils.models import BaseModel


class Payment(BaseModel):
    channel = models.CharField(verbose_name="Канал оплаты", max_length=255, choices=PAYMENT_CHANNEL_CHOICES)
    info = models.JSONField(verbose_name="Информация")
    amount = models.PositiveIntegerField(verbose_name="Сумма")

    class Meta:
        _splash = "Оплат%s"
        verbose_name = _splash % "а"
        verbose_name_plural = _splash % "ы"

    def __str__(self):
        return f'{self.tourist_signup.tour} - {self.amount}'
