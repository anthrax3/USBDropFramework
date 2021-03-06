# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TargetData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.IPAddressField()),
                ('computer_name', models.CharField(max_length=100)),
                ('target_id', models.CharField(max_length=100)),
                ('test_id', models.IntegerField()),
            ],
        ),
    ]
