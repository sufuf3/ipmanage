# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fttb_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fttb_area',
            options={'verbose_name_plural': '1. FTTB \u5340\u57df\u7bc4\u570d'},
        ),
        migrations.AlterModelOptions(
            name='fttb_iplist',
            options={'verbose_name_plural': '2. FTTB IP \u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='fttb_iplist',
            name='phone_2',
            field=models.CharField(default=b'', max_length=18, verbose_name='\u806f\u7d61\u96fb\u8a712', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicalfttb_iplist',
            name='phone_2',
            field=models.CharField(default=b'', max_length=18, verbose_name='\u806f\u7d61\u96fb\u8a712', blank=True),
            preserve_default=True,
        ),
    ]
