# Generated by Django 3.1.1 on 2020-09-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airforcePassWeb', '0004_auto_20200902_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userproperties',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
