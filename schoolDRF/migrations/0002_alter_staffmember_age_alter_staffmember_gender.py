# Generated by Django 4.2.4 on 2023-08-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schoolDRF", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffmember",
            name="age",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="staffmember",
            name="gender",
            field=models.CharField(
                choices=[
                    ("male", "MALE"),
                    ("female", "FEMALE"),
                    ("don't mention", "DON'T MENTION"),
                ],
                max_length=250,
            ),
        ),
    ]
