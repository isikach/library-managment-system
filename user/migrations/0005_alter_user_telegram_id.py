# Generated by Django 5.0.3 on 2024-04-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_telegram_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="telegram_id",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Telegram ID"
            ),
        ),
    ]
