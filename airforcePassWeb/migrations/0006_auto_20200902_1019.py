# Generated by Django 3.1.1 on 2020-09-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airforcePassWeb', '0005_auto_20200902_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='cpf',
            field=models.IntegerField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='userproperties',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
