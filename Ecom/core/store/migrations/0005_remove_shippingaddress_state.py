# Generated by Django 3.2.7 on 2021-10-23 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
    ]