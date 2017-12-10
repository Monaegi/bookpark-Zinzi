# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imp_uid', models.CharField(max_length=50)),
                ('merchant_uid', models.CharField(max_length=50)),
                ('pay_method', models.CharField(max_length=20)),
                ('pg_provider', models.CharField(max_length=20)),
                ('pg_tid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('cancel_amount', models.IntegerField()),
                ('currency', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=10)),
                ('paid_at', models.IntegerField()),
                ('failed_at', models.IntegerField()),
                ('cancelled_at', models.IntegerField()),
                ('fail_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('cancel_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('buyer_name', models.CharField(max_length=10)),
                ('buyer_email', models.CharField(max_length=30)),
                ('buyer_tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('party', models.PositiveSmallIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.ReservationInfo')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='reservation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reservations.Reservation'),
        ),
    ]
