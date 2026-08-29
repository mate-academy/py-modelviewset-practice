from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1), ]
    )
    retired = models.BooleanField()
