# Generated by Django 3.2.4 on 2021-06-21 00:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filtragem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliador', models.IntegerField()),
                ('arquivo', models.CharField(default='', max_length=50)),
                ('histograma', models.CharField(default='', max_length=2000)),
                ('gamma_l', models.FloatField(default=0.01)),
                ('gamma_h', models.FloatField(default=1.0)),
                ('c', models.FloatField(default=0.0)),
                ('d0', models.IntegerField(default=30)),
                ('data_add', models.DateTimeField(default=datetime.datetime(2021, 6, 21, 0, 49, 24, 558692, tzinfo=utc), editable=False)),
            ],
        ),
    ]
