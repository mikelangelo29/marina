# Generated by Django 4.2.3 on 2023-07-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_remove_hotel_item2_remove_hotel_item3'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='sito',
            field=models.URLField(null=True),
        ),
    ]
