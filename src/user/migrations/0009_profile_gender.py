# Generated by Django 4.0.6 on 2022-11-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_profile_last_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('WOMEN', 'WOMEN'), ('MEN', 'MEN')], default='WOMEN', max_length=10),
        ),
    ]
