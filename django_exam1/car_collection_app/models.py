from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

CAR_TYPE = (
    ("Sports Car", "Sorts Car"),
    ("Pickup", "Pickup"),
    ("Crossover", "Crossover"),
    ("Minibus", "Minibus"),
    ("Other", "Other"),
)


def characters_validator(value):
        if len(value) < 2:
            raise ValidationError("The username must be a minimum of 2 chars")


def year_validator(value):
    if 1980 > value > 2049:
        raise ValidationError("TYear must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[characters_validator])
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(18)])
    password = models.CharField(max_length=30, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)


class Car(models.Model):
    car_type = models.CharField(max_length=10, choices=CAR_TYPE)
    car_model = models.CharField(max_length=20, null=False, blank=False, validators=[MinLengthValidator(2)])
    year = models.IntegerField(null=False, blank=False, validators=[year_validator])
    image_url = models.URLField(verbose_name='Image URL:')
    price = models.FloatField(validators=[MinValueValidator(1)])


