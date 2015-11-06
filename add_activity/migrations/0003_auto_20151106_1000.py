# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_activity', '0002_auto_20151106_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='formInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_count', models.CharField(max_length=100000, null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
