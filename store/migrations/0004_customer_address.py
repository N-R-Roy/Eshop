# Generated by Django 4.0.1 on 2022-04-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=250),
        ),
    ]
