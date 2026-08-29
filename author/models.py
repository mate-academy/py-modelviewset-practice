from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField()
    retired = models.BooleanField()

    def __str__(self) -> str:
        return (
            self.pseudonym
            if self.pseudonym
            else f"{self.first_name} {self.last_name}"
        )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"
