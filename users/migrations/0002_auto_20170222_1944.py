# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.TextField()),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='citizenaadhar',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='citizenaadhar',
            name='citizen_profile',
        ),
        migrations.AlterUniqueTogether(
            name='citizenphonenumber',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='citizenphonenumber',
            name='citizen_profile',
        ),
        migrations.RemoveField(
            model_name='citizenprofile',
            name='authorised',
        ),
        migrations.RemoveField(
            model_name='citizenprofile',
            name='blocked',
        ),
        migrations.RemoveField(
            model_name='citizenprofile',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='citizenprofile',
            name='signup_done',
        ),
        migrations.RemoveField(
            model_name='citizenprofile',
            name='signup_stage',
        ),
        migrations.RemoveField(
            model_name='govofficerprofile',
            name='authorised',
        ),
        migrations.RemoveField(
            model_name='govofficerprofile',
            name='authorization_level',
        ),
        migrations.DeleteModel(
            name='CitizenAadhar',
        ),
        migrations.DeleteModel(
            name='CitizenPhoneNumber',
        ),
        migrations.AddField(
            model_name='govofficerprofile',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.DepartmentProfile'),
            preserve_default=False,
        ),
    ]