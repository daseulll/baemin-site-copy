# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-25 06:11
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0007_auto_20190119_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='partner/menu'),
            preserve_default=False,
        ),
    ]
