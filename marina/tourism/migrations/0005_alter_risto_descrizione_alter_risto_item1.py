# Generated by Django 4.2.3 on 2023-07-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0004_risto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risto',
            name='descrizione',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AlterField(
            model_name='risto',
            name='item1',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
