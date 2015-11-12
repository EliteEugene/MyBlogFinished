# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20151022_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsersBlog',
        ),
    ]
