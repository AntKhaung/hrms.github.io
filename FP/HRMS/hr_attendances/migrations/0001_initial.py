# Generated by Django 2.0 on 2023-07-02 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('check_in', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Check In')),
                ('check_out', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Check Out')),
            ],
        ),
    ]