# Generated by Django 2.2.6 on 2019-10-12 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jikkyotter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 23, 39, 56, 24441), verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 23, 39, 56, 26018), verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 23, 39, 56, 25999), verbose_name='開始日時'),
        ),
    ]
