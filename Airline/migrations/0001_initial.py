# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-04 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_seats', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Travelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=30)),
                ('from_place', models.CharField(max_length=30)),
                ('to_place', models.CharField(max_length=30)),
                ('depart_at_from', models.TimeField()),
                ('arrival_at_to', models.TimeField()),
                ('seat_no', models.IntegerField(max_length=100)),
                ('available', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('off', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Travelling',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airline.Travelling'),
        ),
        migrations.AddField(
            model_name='booking',
            name='booked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
