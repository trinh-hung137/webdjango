# Generated by Django 3.2.7 on 2021-11-19 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_orderitem_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='translation_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='date_added',
        ),
    ]
