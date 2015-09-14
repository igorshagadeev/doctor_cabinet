# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='имя', default='', max_length=128)),
                ('surname', models.CharField(verbose_name='фамилия', default='', max_length=128)),
                ('patronymic', models.CharField(verbose_name='отчество', default='', max_length=128)),
                ('datetime', models.DateTimeField(verbose_name='Дата')),
                ('doctor', models.ForeignKey(blank=True, related_name='doctor', null=True, to='doctor.Doctor')),
            ],
        ),
    ]
