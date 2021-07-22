# Generated by Django 3.2.4 on 2021-06-22 00:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hmrxapp', '0001_cria_tabela_filtragem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtragem',
            name='data_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 0, 14, 46, 624188, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='filtragem',
            name='histograma',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
