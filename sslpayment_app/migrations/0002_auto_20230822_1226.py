# Generated by Django 3.2 on 2023-08-22 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sslpayment_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_info',
            name='email',
        ),
        migrations.RemoveField(
            model_name='payment_info',
            name='name',
        ),
        migrations.RemoveField(
            model_name='payment_info',
            name='phone_number',
        ),
    ]
