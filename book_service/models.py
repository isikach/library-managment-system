from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cover(models.TextChoices):
    HARD = "Hard"
    SOFT = "Soft"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=4, choices=Cover.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1000.00)]
    )

    def __str__(self):
        return self.title
