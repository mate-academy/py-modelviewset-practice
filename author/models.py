from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField()
    retired = models.BooleanField(default=False)

    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self) -> str:
        return self.pseudonym or f"{self.first_name} {self.last_name}"
