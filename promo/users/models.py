from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from promo.promos.models import Promo


class User(AbstractUser):
    class Type(models.TextChoices):
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        NORMAL = "NORMAL", "Normal"

    base_type = Type.NORMAL

    type = models.CharField(
        "User Type",
        max_length=50,
        choices=Type.choices,
        null=True,
        default=base_type,
    )
    name = models.CharField(_("Name"), blank=True, max_length=255)
    address = models.CharField(_("Address"), max_length=100, blank=True, null=True)
    mobile_number = models.CharField(
        _("Mobile Number"), max_length=32, blank=True, null=True, unique=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "users"

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.type == "ADMINISTRATOR"

    @property
    def is_normal(self):
        return self.type == "NORMAL"


class AdministratorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(type=User.Type.ADMINISTRATOR)
        )


class AdministratorUser(User):
    base_type = User.Type.ADMINISTRATOR
    objects = AdministratorManager()

    class Meta:
        proxy = True

    verbose_name = "Administrator User"
    verbose_name_plural = "Administrator Users"


class NormalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.NORMAL)


class NormalUser(User):
    base_type = User.Type.NORMAL
    objects = NormalManager()

    class Meta:
        proxy = True

    verbose_name = "Normal User"
    verbose_name_plural = "Normal Users"