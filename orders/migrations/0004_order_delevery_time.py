# Generated by Django 4.2.3 on 2023-09-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_tax_order_shipping_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delevery_time',
            field=models.IntegerField(default=0),
        ),
    ]
