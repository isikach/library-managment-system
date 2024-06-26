# Generated by Django 5.0.3 on 2024-04-03 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="daily_fee",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(1000.0),
                ],
            ),
        ),
    ]
