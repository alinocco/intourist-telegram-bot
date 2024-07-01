from django.conf import settings
from django.db import models

from modules.payments.models import Payment
from modules.signups.consts import TOURIST_SIGNUPS_STATUSES
from modules.tours.models import TourInstance
from modules.utils.models import BaseModel


class TouristSignup(BaseModel):
    tour_instance = models.ForeignKey(TourInstance, on_delete=models.PROTECT, related_name="tourist_signups")
    tourist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="tourist_signups")
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, related_name="tourist_signup")
    status = models.CharField(verbose_name="Статус", max_length=255, choices=TOURIST_SIGNUPS_STATUSES,
                              default=TOURIST_SIGNUPS_STATUSES.reserved)
    people_quantity = models.PositiveIntegerField(verbose_name="Количество людей", default=1)
    reserved_till = models.DateTimeField(verbose_name="Бронь до", null=True, blank=True)

    class Meta:
        _splash = "Запис%s на тур"
        verbose_name = _splash % "ь"
        verbose_name_plural = _splash % "и"
