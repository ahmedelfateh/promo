from datetime import datetime
from typing import Type
from django.utils import timezone
from django.db import models

# from promo.users.models import User

# Create your models here.
class Promo(models.Model):
    class Type(models.TextChoices):
        CONSTANT_VALUE = "CV", "Constant Value"
        PERCENT = "P", "Percent"

    promo_type = models.CharField(
        "Promo Type", max_length=2, choices=Type.choices, null=True
    )
    promo_code = models.CharField("Promo Code", max_length=10, null=True, unique=True)
    creation_time = models.DateField("Created At", auto_now_add=True)
    start_time = models.DateField("Start Time", blank=False)
    end_time = models.DateField("End Time", blank=False)
    promo_amount = models.IntegerField("Promo Amount")
    is_active = models.BooleanField("Active", default=True)
    description = models.TextField("Description", blank=True)
    user = models.ForeignKey(
        "users.User",
        related_name="promos",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Promo"
        verbose_name_plural = "Promos"
        db_table = "promos"

    def __str__(self):
        return self.promo_code

    @property
    def is_expired(self):
        return self.end_time < datetime.date(timezone.now())
