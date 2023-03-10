# Generated by Django 4.0.6 on 2022-11-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_category_name_de_category_name_en_category_name_tr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_tr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_zn_ch',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
