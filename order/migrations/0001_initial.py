# Generated by Django 2.0.6 on 2018-07-20 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Order total (INR)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('emailAddress', models.EmailField(max_length=255, verbose_name='E-mail Address')),
                ('shippingName', models.CharField(max_length=255)),
                ('shippingAddressLine1', models.CharField(max_length=255)),
                ('shippingAddressLine2', models.CharField(max_length=255)),
                ('shippingState', models.CharField(max_length=255)),
                ('shippingCity', models.CharField(max_length=255)),
                ('shippingPincode', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Product Price (INR)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
                'db_table': 'OrderItem',
            },
        ),
    ]