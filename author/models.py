from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, db_index=True)
    pseudonym = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True
    )
    birth_date = models.DateField(null=True, blank=True)
    retired = models.BooleanField(default=False)
    age = models.IntegerField(null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
