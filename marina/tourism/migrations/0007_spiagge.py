# Generated by Django 4.2.3 on 2023-07-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0006_remove_hotel_sito_remove_risto_sito_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spiagge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('titolo', models.CharField(default=None, max_length=50)),
                ('descrizione', models.CharField(default=None, max_length=250)),
                ('item1', models.CharField(default=None, max_length=250)),
            ],
        ),
    ]
