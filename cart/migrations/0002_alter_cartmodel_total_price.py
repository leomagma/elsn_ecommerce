# Generated by Django 5.1.4 on 2025-01-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='total_price',
            field=models.PositiveIntegerField(auto_created=True),
        ),
    ]
