# Generated by Django 4.0.3 on 2022-03-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_clothes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
