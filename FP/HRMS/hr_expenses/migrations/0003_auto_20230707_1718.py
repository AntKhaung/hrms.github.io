# Generated by Django 2.0 on 2023-07-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_expenses', '0002_auto_20230707_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='paid_by',
            field=models.CharField(default='other', max_length=50, verbose_name='Paid By'),
        ),
    ]
