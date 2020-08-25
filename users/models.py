from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    key1 = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="user_key1",
    )
    key2 = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=2,
        on_delete=models.SET_DEFAULT,
        related_name="user_key2",
    )
    key3 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        default=3,
        on_delete=models.SET_DEFAULT,
        related_name="user_key3",
    )
    key4 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        default=4,
        on_delete=models.SET_DEFAULT,
        related_name="user_key4",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
