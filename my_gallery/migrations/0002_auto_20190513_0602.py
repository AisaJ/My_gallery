# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-13 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='children.jpg', upload_to='image/'),
        ),
    ]
