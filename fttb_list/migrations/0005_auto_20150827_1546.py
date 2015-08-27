# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fttb_list', '0004_auto_20150827_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fttb_area',
            name='gateway',
            field=models.GenericIPAddressField(verbose_name='Gateway'),
        ),
        migrations.AlterField(
            model_name='fttb_iplist',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='historicalfttb_iplist',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
