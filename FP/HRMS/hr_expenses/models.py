from django.db import models
from django.utils import timezone

# Create your models here.

class ExpenseModel(models.Model):
	description = models.CharField(max_length=100, verbose_name='Description')
	product = models.CharField(max_length=100, verbose_name='Product')
	expense_date = models.DateField(verbose_name='Expense Date', default=timezone.now)
	note = models.TextField(max_length=100, verbose_name='Note')
	total_ammount = models.CharField(max_length=20, verbose_name='total_ammount', default=None)
	paid_by = models.CharField(max_length=50, verbose_name='Paid By', default='other')
	attachment = models.ImageField(verbose_name='Image', default=None)
