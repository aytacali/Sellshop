# Generated by Django 4.1 on 2022-10-19 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 12, 12, 20, 735868)),
        ),
    ]