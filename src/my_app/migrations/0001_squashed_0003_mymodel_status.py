# Generated by Django 2.0.5 on 2018-06-12 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('my_app', '0001_initial'), ('my_app', '0002_auto_20180523_1720'), ('my_app', '0003_mymodel_status')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('change_time', models.DateTimeField(blank=True, null=True)),
                ('text', models.CharField(blank=True, default='', max_length=150)),
                ('random_text', models.CharField(blank=True, default='', max_length=150)),
                ('status', models.CharField(choices=[('new', 'new'), ('progress', 'progress'), ('done', 'done')], default='new', max_length=20)),
            ],
        ),
    ]
