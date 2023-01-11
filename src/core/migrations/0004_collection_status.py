# Generated by Django 4.0.6 on 2022-11-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=50),
        ),
    ]
