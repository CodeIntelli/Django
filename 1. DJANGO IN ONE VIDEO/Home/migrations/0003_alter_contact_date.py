# Generated by Django 3.2.4 on 2021-06-24 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(1111, 11, 11, 0, 0), help_text='Today Date.', null=True),
        ),
    ]
