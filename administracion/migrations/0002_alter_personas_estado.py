# Generated by Django 4.2.1 on 2023-06-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administracion", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personas",
            name="estado",
            field=models.CharField(max_length=100),
        ),
    ]
