# Generated by Django 4.0.3 on 2022-03-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_clothes_delete_jacket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='brand',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
