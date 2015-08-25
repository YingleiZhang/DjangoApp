# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
