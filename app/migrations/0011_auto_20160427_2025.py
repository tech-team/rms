# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='type',
            field=models.CharField(choices=[('\u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0439', '\u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0439'), ('\u0431\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u044b\u0439', '\u0431\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u044b\u0439')], default='\u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0439', max_length=10),
        ),
    ]
