# Generated by Django 2.1.7 on 2019-02-25 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190224_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 25, 2, 54, 2, 190710)),
        ),
    ]
