# Generated by Django 4.2.3 on 2023-07-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Natura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('titolo', models.CharField(default=None, max_length=50)),
                ('descrizione', models.CharField(default=None, max_length=250)),
                ('item1', models.CharField(default=None, max_length=250)),
            ],
        ),
    ]
