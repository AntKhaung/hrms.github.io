# Generated by Django 2.0 on 2023-07-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_attendances', '0003_attendancemodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancemodel',
            name='description',
            field=models.CharField(default=None, max_length=100, verbose_name='Description'),
        ),
    ]
