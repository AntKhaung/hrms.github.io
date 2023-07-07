from django.db import models
from django.utils import timezone
# Create your models here.


class AttendanceModel(models.Model):
	 name = models.CharField(max_length=20, verbose_name='Name')
	 check_in = models.TimeField(verbose_name='Check In', default=timezone.now)
	 check_out = models.TimeField(verbose_name='Check Out', default=timezone.now)
	 date = models.DateField(verbose_name='Date', default=None)
	 description = models.CharField(max_length=100, verbose_name='Description', default=None)
