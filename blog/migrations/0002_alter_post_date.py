# Generated by Django 4.1.3 on 2022-12-01 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 12, 35, 31, 40716, tzinfo=datetime.timezone.utc)),
        ),
    ]