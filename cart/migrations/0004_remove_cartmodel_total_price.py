# Generated by Django 5.1.4 on 2025-01-09 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartmodel_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='total_price',
        ),
    ]
