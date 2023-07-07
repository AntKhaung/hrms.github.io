from django import forms
from django.forms import widgets
from django.utils import timezone

class AttendanceForm(forms.Form):
	name = forms.CharField(max_length=20, label='Enter Name', widget=widgets.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control'}))
	check_in = forms.TimeField(label='Check In', widget=widgets.TimeInput(attrs={'type':'time' , 'class': 'form-control'}))
	check_out = forms.TimeField(label='Check Out', widget=widgets.TimeInput(attrs={'type':'time' , 'class': 'form-control'}))
	date = forms.DateField(label='Enter Date', widget=widgets.DateInput(attrs={'type':'date' , 'class': 'form-control'}))
	description = forms.CharField(max_length=100, label='Enter Description', widget=widgets.TextInput(attrs={'placeholder':'Description here...', 'class': 'form-control'}))
