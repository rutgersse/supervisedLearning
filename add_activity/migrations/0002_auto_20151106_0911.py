# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_activity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='ask_activity',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ask_top_attribute',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count',
            field=models.CharField(max_length=100000, null=True, blank=True),
        ),
    ]
