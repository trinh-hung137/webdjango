# Generated by Django 3.2.7 on 2021-11-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]