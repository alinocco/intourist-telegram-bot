from django.conf import settings
from django.db import models

from modules.tours.consts import COMPLEXITY_CHOICES, TOUR_INSTANCE_STATUSES
from modules.utils.models import BaseModel


class Location(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    longitude = models.DecimalField(verbose_name="Долгота", max_digits=9, decimal_places=5)
    latitude = models.DecimalField(verbose_name="Широта", max_digits=9, decimal_places=5)

    class Meta:
        _splash = "Локаци%s"
        verbose_name = _splash % "я"
        verbose_name_plural = _splash % "и"


class Tour(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.PositiveIntegerField(verbose_name="Цена")
    complexity = models.CharField(verbose_name="Сложность", max_length=255, choices=COMPLEXITY_CHOICES)
    locations = models.ManyToManyField(Location, through="TourLocation", related_name="tours")
    program = models.JSONField(verbose_name="Программа", blank=True, null=True)
    schedule = models.JSONField(verbose_name="Расписание", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Расписание активировано", default=True)

    class Meta:
        _splash = "Тур%s"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"


class TourLocation(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(verbose_name="Порядок", default=1)

    class Meta:
        _splash = "Локаци%s туров"
        verbose_name = _splash % "я"
        verbose_name_plural = _splash % "и"


class Guide(BaseModel):
    name = models.CharField(verbose_name="Имя", max_length=255)

    class Meta:
        _splash = "Гид%s"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"


class TourInstance(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, related_name="tour_instances")
    guides = models.ManyToManyField(Guide, related_name="tour_instances")
    date = models.DateField(verbose_name="Дата")
    status = models.CharField(verbose_name="Статус", max_length=255, choices=TOUR_INSTANCE_STATUSES)
    telegram_group = models.URLField(verbose_name="Telegram группа", max_length=255)
    whatsapp_group = models.URLField(verbose_name="WhatsApp группа", max_length=255)

    maximum_people = models.PositiveIntegerField(verbose_name="Максимум человек",
                                                 default=settings.DEFAULT_MAX_PEOPLE_PER_TOUR)

    class Meta:
        _splash = "Отдельный тур%s"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"
