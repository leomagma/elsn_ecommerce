# Generated by Django 5.1.4 on 2025-01-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]
