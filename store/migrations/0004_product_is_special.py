# Generated by Django 4.2.3 on 2023-09-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_id_alter_reviewrating_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
