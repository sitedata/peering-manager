# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-21 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb', '0003_networkixlan_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networkixlan',
            options={'ordering': ['asn', 'ipaddr6', 'ipaddr4'], 'verbose_name': 'Network IX LAN', 'verbose_name_plural': 'Network IX LANs'},
        ),
    ]
