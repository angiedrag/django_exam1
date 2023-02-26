from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

CAR_TYPE = (
    ("Sport Car", "Sport Car"),
    ("Pickup", "Pickup"),
    ("Crossover", "Crossover"),
    ("Minibus", "Minibus"),
    ("Other", "Other"),
)


def characters_validator(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(max_length=9, validators=[characters_validator],)
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(18)],)
    password = models.CharField(max_length=30,)
    first_name = models.CharField(max_length=30, null=True, blank=True,)
    last_name = models.CharField(max_length=30, null=True, blank=True,)
    profile_picture = models.URLField(null=True, blank=True,)


class Car(models.Model):
    car_type = models.CharField(max_length=10, choices=CAR_TYPE)
    car_model = models.CharField(validators=[MinLengthValidator(2)], max_length=20)
    year = models.IntegerField(validators=[year_validator])
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(1),])


