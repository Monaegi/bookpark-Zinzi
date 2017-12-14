# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20171212_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationCancel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('tax_free', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservations.Payment')),
            ],
        ),
    ]
