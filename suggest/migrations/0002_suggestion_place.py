# Generated by Django 3.1.5 on 2021-08-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='place',
            field=models.IntegerField(default=0),
        ),
    ]
