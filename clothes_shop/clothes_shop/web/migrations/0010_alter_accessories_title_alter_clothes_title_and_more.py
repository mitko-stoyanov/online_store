# Generated by Django 4.0.3 on 2022-04-10 16:33

import clothes_shop.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_clothes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='title',
            field=models.CharField(max_length=30, validators=[clothes_shop.web.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='title',
            field=models.CharField(max_length=30, validators=[clothes_shop.web.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20, validators=[clothes_shop.web.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='title',
            field=models.CharField(max_length=30, validators=[clothes_shop.web.validators.validate_only_letters]),
        ),
    ]