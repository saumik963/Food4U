# Generated by Django 4.2.3 on 2023-09-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_delevery_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delevery_time',
        ),
    ]
