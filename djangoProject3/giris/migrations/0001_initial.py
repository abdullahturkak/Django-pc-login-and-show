# Generated by Django 3.1.5 on 2021-01-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Satıs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marka', models.CharField(max_length=60, verbose_name='marka')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
                ('fiyat', models.CharField(max_length=50, verbose_name='fiyat')),
                ('tel', models.CharField(blank=True, max_length=20, verbose_name='tel')),
                ('adres', models.TextField(blank=True, verbose_name='adres')),
            ],
        ),
    ]
