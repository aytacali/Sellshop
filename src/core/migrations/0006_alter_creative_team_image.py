# Generated by Django 4.0.6 on 2022-11-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creative_team',
            name='image',
            field=models.ImageField(upload_to='team'),
        ),
    ]