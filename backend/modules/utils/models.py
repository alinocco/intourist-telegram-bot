from django.db import models


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True
