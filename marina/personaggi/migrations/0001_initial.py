# Generated by Django 4.2.3 on 2023-07-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaggi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('titolo', models.CharField(default=None, max_length=50)),
                ('descrizione', models.CharField(default=None, max_length=150)),
                ('item1', models.TextField(default=None)),
            ],
        ),
    ]
