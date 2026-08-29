from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField()
    retired = models.BooleanField()

    class Meta:
        ordering = ("first_name",)

    def __str__(self):
        return f"{self.first_name}" \
               f" {self.last_name}" \
               f" {self.pseudonym}" \
               f" {self.age}"
