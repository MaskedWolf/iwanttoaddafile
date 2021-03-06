# Generated by Django 3.1.5 on 2021-08-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sopdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('JOHOR', 'Johor'), ('KEDAH', 'Kedah'), ('KELANTAN', 'Kelantan'), ('MALACCA', 'Malacca'), ('NEGERI SEMBILAN', 'Negeri Sembilan'), ('PAHANG', 'Pahang'), ('PENANG', 'Penang'), ('PERAK', 'Perak'), ('PERLIS', 'Perlis'), ('SABAH', 'Sabah'), ('SARAWAK', 'Sarawak'), ('SELANGOR', 'Selangor'), ('TERENGGANU', 'Terengganu'), ('KUALA LUMPUR', 'Kuala Lumpur'), ('LABUAN', 'Labuan'), ('PUTRAJAYA', 'Putrajaya')], max_length=50, null=True)),
                ('phase', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], null=True)),
                ('Description_dining_vaccinated', models.CharField(max_length=200, null=True)),
                ('Description_dining_unvaccinated', models.CharField(max_length=200, null=True)),
                ('Description_travel', models.CharField(max_length=200, null=True)),
                ('Description_transport', models.CharField(max_length=200, null=True)),
                ('Description_religion', models.CharField(max_length=200, null=True)),
                ('Description_market', models.CharField(max_length=200, null=True)),
                ('Description_shopping', models.CharField(max_length=200, null=True)),
                ('crtDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
