from django.db import models


class Mentor(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.PositiveSmallIntegerField()
    available = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
