from django.db import models

from rest_framework.reverse import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField()
    retired = models.BooleanField()
