# Generated by Django 2.0.6 on 2018-07-20 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_address_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
    ]
