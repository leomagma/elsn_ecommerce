# Generated by Django 5.1.4 on 2025-01-09 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cartmodel_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
