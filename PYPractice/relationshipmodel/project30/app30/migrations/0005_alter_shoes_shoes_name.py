# Generated by Django 3.2.7 on 2021-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app30', '0004_auto_20211110_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='shoes_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]