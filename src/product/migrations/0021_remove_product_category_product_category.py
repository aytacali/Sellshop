# Generated by Django 4.0.6 on 2022-11-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
