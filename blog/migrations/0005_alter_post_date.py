# Generated by Django 4.1.3 on 2022-12-02 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 9, 4, 32, 791086, tzinfo=datetime.timezone.utc)),
        ),
    ]
