# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.CharField(blank=True, choices=[('kor', 'Korean'), ('chn', 'Chinese'), ('jpn', 'Japanese'), ('mex', 'Mexican'), ('amc', 'American'), ('tha', 'Thai'), ('med', 'Mediterranean'), ('ita', 'Italian'), ('vtn', 'Vietnamese'), ('spn', 'Spanish'), ('ind', 'Indian'), ('etc', 'Etc')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=10, unique=True)),
                ('user_type', models.CharField(choices=[('e', 'Email'), ('f', 'Facebook')], default='e', max_length=1)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user')),
                ('is_owner', models.BooleanField(default=False)),
                ('joined_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
