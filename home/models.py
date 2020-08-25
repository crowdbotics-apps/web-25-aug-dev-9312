from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    tests = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_tests",
    )
    user = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=2,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_user",
    )
    new = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_new",
    )
    test = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_test",
    )
    key2 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_key2",
    )
    key1 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        default=2,
        on_delete=models.SET_DEFAULT,
        related_name="customtext_key1",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
