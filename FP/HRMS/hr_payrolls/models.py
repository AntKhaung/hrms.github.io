from django.db import models
from django.utils import timezone

# Create your models here.

class PayrollModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	ammount = models.CharField(max_length=100, verbose_name='Total Ammount')
	note = models.TextField(max_length=100, verbose_name='Enter Note')
	status = models.CharField(max_length=50, verbose_name='Status', default='other')
	is_paid = models.BooleanField(verbose_name='Is Paid', default=False)
	date = models.DateField(verbose_name='Enter Date', default=timezone.now)
	attachment = models.ImageField(verbose_name='Image', default=None)
