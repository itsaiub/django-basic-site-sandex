# Generated by Django 2.2.3 on 2019-07-26 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 26, 8, 15, 10, 522018), verbose_name='date published'),
        ),
    ]