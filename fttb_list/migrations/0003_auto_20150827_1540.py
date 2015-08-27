# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fttb_list', '0002_auto_20150728_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fttb_iplist',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='E-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalfttb_iplist',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='E-mail', blank=True),
        ),
    ]
