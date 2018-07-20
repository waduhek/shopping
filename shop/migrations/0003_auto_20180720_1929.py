# Generated by Django 2.0.6 on 2018-07-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180708_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model_number',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_duration',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_type',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
