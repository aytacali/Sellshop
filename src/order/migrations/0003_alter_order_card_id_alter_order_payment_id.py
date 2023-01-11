# Generated by Django 4.0.6 on 2022-11-21 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_card_user_id_alter_wish_list_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.card'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.payment_method'),
        ),
    ]
