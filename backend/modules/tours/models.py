from datetime import datetime

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils.dates import WEEKDAYS
from multiselectfield.db.fields import MultiSelectField

from modules.tours.consts import COMPLEXITY_CHOICES, TOUR_INSTANCE_STATUSES
from modules.tours.utils import schedule_dates_in_period
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
    locations = models.ManyToManyField(Location, verbose_name="Локации", through="TourLocation", related_name="tours")
    program = models.JSONField(verbose_name="Программа", blank=True, null=True)
    schedule = MultiSelectField(verbose_name="Расписание создания", choices=WEEKDAYS, blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Расписание активировано", default=True)

    class Meta:
        _splash = "Тур%s"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"

    def __str__(self):
        return self.name

    @property
    def schedule_as_integers(self):
        return [int(day) for day in self.schedule]

    def create_tour_instances_for_period(self, start_date: datetime, end_date: datetime):
        for date in schedule_dates_in_period(self.schedule_as_integers, start_date, end_date):
            TourInstance.objects.create(tour=self, date=date)


class TourLocation(BaseModel):
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name="Локация", on_delete=models.CASCADE)
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
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, verbose_name="Тур", related_name="tour_instances")
    guides = models.ManyToManyField(Guide, verbose_name="Гиды", related_name="tour_instances")
    date = models.DateField(verbose_name="Дата")
    status = models.CharField(verbose_name="Статус", max_length=255, choices=TOUR_INSTANCE_STATUSES,
                              default=TOUR_INSTANCE_STATUSES.pending)
    telegram_group = models.URLField(verbose_name="Telegram группа", max_length=255, null=True, blank=True)
    whatsapp_group = models.URLField(verbose_name="WhatsApp группа", max_length=255, null=True, blank=True)

    maximum_people = models.PositiveIntegerField(verbose_name="Максимум человек",
                                                 default=settings.DEFAULT_MAX_PEOPLE_PER_TOUR)

    class Meta:
        _splash = "Отдельны%s тур%s"
        verbose_name = _splash % ("й", "")
        verbose_name_plural = _splash % ("е", "ы")

    def __str__(self):
        return f"{self.date} {self.tour.name}"

    @property
    def current_people_quantity(self):
        return self.tourist_signups.aggregate(people_quantity=Sum("people_quantity", default=0))["people_quantity"]

    current_people_quantity.fget.short_description = "Текущее количество человек"

    def is_available(self, people_quantity):
        return self.current_people_quantity + people_quantity <= self.maximum_people
