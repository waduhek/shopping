# Generated by Django 2.0.6 on 2018-07-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_address_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
