# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='fttb_area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(default=b'', max_length=10, verbose_name='\u5340\u57df')),
                ('ip_range', models.CharField(default=b'', max_length=35, verbose_name='IP Range')),
                ('subnet_mask', models.IPAddressField(verbose_name='Subnet Mask')),
                ('gateway', models.IPAddressField(verbose_name='Gateway')),
                ('dns', models.CharField(default=b'', max_length=35, verbose_name='DNS', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fttb_iplist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField()),
                ('applicant', models.CharField(default=b'', max_length=30, verbose_name='\u7533\u8acb\u4eba', blank=True)),
                ('customer', models.CharField(default=b'', max_length=30, verbose_name='\u5ba2\u6236\u540d\u7a31', blank=True)),
                ('ID_no', models.CharField(default=b'', max_length=15, verbose_name='\u6559\u8077\u54e1\u7de8\u865f/\u5b78\u865f', blank=True)),
                ('new_ID_no', models.CharField(default=b'', max_length=15, verbose_name='\u78a9(\u535a)\u73ed\u65b0\u5b78\u865f', blank=True)),
                ('apply_type', models.CharField(default=b'', max_length=25, verbose_name='\u7533\u8acb\u578b\u614b', blank=True)),
                ('attach_phone', models.CharField(default=b'', max_length=15, verbose_name='\u9644\u639b\u96fb\u8a71', blank=True)),
                ('cellphone', models.CharField(default=b'', max_length=12, verbose_name='\u624b\u6a5f', blank=True)),
                ('phone_2', models.CharField(default=b'', max_length=15, verbose_name='\u806f\u7d61\u96fb\u8a712', blank=True)),
                ('addr', models.CharField(default=b'', max_length=50, verbose_name='\u88dd\u6a5f\u5730\u5740', blank=True)),
                ('rate', models.CharField(default=b'', max_length=15, verbose_name='\u901f\u7387', blank=True)),
                ('apply_date', models.DateField(null=True, verbose_name='\u7533\u8acb\u65e5\u671f', blank=True)),
                ('allotte_time', models.DateField(null=True, verbose_name='\u5206\u914d\u65e5\u671f', blank=True)),
                ('email', models.EmailField(default=b'', max_length=75, verbose_name='E-mail', blank=True)),
                ('circuit_no', models.CharField(default=b'', max_length=10, verbose_name='\u96fb\u8def\u7de8\u865f', blank=True)),
                ('completion_isnt', models.DateField(null=True, verbose_name='\u662f\u5426\u7ae3\u5de5', blank=True)),
                ('notice', models.CharField(default=b'N', max_length=1, verbose_name='\u662f\u5426\u901a\u77e5IP', blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('note', models.TextField(default=b'', max_length=500, verbose_name='\u5099\u8a3b', blank=True)),
                ('area', models.ForeignKey(verbose_name='\u5340\u57df', to='fttb_list.fttb_area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Historicalfttb_iplist',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('ip', models.IPAddressField()),
                ('applicant', models.CharField(default=b'', max_length=30, verbose_name='\u7533\u8acb\u4eba', blank=True)),
                ('customer', models.CharField(default=b'', max_length=30, verbose_name='\u5ba2\u6236\u540d\u7a31', blank=True)),
                ('ID_no', models.CharField(default=b'', max_length=15, verbose_name='\u6559\u8077\u54e1\u7de8\u865f/\u5b78\u865f', blank=True)),
                ('new_ID_no', models.CharField(default=b'', max_length=15, verbose_name='\u78a9(\u535a)\u73ed\u65b0\u5b78\u865f', blank=True)),
                ('apply_type', models.CharField(default=b'', max_length=25, verbose_name='\u7533\u8acb\u578b\u614b', blank=True)),
                ('attach_phone', models.CharField(default=b'', max_length=15, verbose_name='\u9644\u639b\u96fb\u8a71', blank=True)),
                ('cellphone', models.CharField(default=b'', max_length=12, verbose_name='\u624b\u6a5f', blank=True)),
                ('phone_2', models.CharField(default=b'', max_length=15, verbose_name='\u806f\u7d61\u96fb\u8a712', blank=True)),
                ('addr', models.CharField(default=b'', max_length=50, verbose_name='\u88dd\u6a5f\u5730\u5740', blank=True)),
                ('rate', models.CharField(default=b'', max_length=15, verbose_name='\u901f\u7387', blank=True)),
                ('apply_date', models.DateField(null=True, verbose_name='\u7533\u8acb\u65e5\u671f', blank=True)),
                ('allotte_time', models.DateField(null=True, verbose_name='\u5206\u914d\u65e5\u671f', blank=True)),
                ('email', models.EmailField(default=b'', max_length=75, verbose_name='E-mail', blank=True)),
                ('circuit_no', models.CharField(default=b'', max_length=10, verbose_name='\u96fb\u8def\u7de8\u865f', blank=True)),
                ('completion_isnt', models.DateField(null=True, verbose_name='\u662f\u5426\u7ae3\u5de5', blank=True)),
                ('notice', models.CharField(default=b'N', max_length=1, verbose_name='\u662f\u5426\u901a\u77e5IP', blank=True, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('note', models.TextField(default=b'', max_length=500, verbose_name='\u5099\u8a3b', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('area', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='fttb_list.fttb_area', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical fttb_iplist',
            },
            bases=(models.Model,),
        ),
    ]
