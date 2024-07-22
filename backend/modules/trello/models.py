from django.db import models

from modules.signups.models import TouristSignup
from modules.tours.models import TourInstance
from modules.utils.models import BaseModel


class TrelloMapperBaseModel(BaseModel):
    trello_id = models.CharField(verbose_name="Trello ID", max_length=30)
    trello_data = models.JSONField(verbose_name="Данные в Trello")

    class Meta:
        abstract = True


class TrelloTourInstanceMapper(TrelloMapperBaseModel):
    tour_instance = models.OneToOneField(TourInstance, on_delete=models.PROTECT, verbose_name="Тур",
                                         related_name="trello_integration")

    class Meta:
        _splash = "Тур%s в Trello"
        verbose_name = _splash % ""
        verbose_name_plural = _splash % "ы"


class TrelloTouristSignupMapper(TrelloMapperBaseModel):
    # utilize foreign key because one tourist signup can be paid for a few people
    tourist_signup = models.ForeignKey(TouristSignup, on_delete=models.PROTECT, verbose_name="Запись на тур",
                                       related_name="trello_integration")

    class Meta:
        _splash = "Запис%s на тур в Trello"
        verbose_name = _splash % "ь"
        verbose_name_plural = _splash % "и"
