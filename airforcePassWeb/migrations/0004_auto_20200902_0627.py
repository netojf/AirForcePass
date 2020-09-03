# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airforcePassWeb', '0003_userproperties_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='userproperties',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='userproperties',
            name='saram',
            field=models.CharField(max_length=15),
        ),
    ]
