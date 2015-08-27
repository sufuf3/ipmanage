# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fttb_list', '0003_auto_20150827_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fttb_area',
            name='subnet_mask',
            field=models.GenericIPAddressField(verbose_name='Subnet Mask'),
        ),
    ]
