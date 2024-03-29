# Generated by Django 3.2 on 2023-08-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgd_consultancy_app', '0005_alter_companyinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='address',
            field=models.TextField(default=1, max_length=200, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]
