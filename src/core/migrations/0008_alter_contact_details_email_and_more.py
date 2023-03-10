# Generated by Django 4.0.6 on 2022-11-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_contact_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='phone_number',
            field=models.CharField(max_length=128),
        ),
    ]
