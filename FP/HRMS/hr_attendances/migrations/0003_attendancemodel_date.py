# Generated by Django 2.0 on 2023-07-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_attendances', '0002_auto_20230703_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancemodel',
            name='date',
            field=models.DateField(default=None, verbose_name='Date'),
        ),
    ]
