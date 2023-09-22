from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Directors(models.Model):
    class Genders(models.TextChoices):
        MALE = 1, _("Male")
        FEMALE = 2, _("Female")
    name = models.CharField(max_length=200)
    gender = models.IntegerField(default=Genders.MALE, choices=Genders.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
