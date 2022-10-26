from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    retired = models.BooleanField()
    age = models.IntegerField()
