# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_question_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_title',
        ),
    ]
