# Generated by Django 4.2.3 on 2023-07-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_data_creazione'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-data_creazione']},
        ),
    ]
