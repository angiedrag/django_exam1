# Generated by Django 3.2.18 on 2023-02-26 15:08

from django.db import migrations, models
import django_exam1.car_collection_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('car_collection_app', '0002_auto_20230226_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Sport Car', 'Sport Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=9, validators=[django_exam1.car_collection_app.models.characters_validator]),
        ),
    ]
