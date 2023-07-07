from django import forms
from hr_payrolls import models
from django.forms import widgets

STATUS_CHOICES =(
	('Employee', 'Employee'),
	('Customer', 'Customer')
)

class PayrollForm(forms.ModelForm):

	class Meta:
		model = models.PayrollModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'ammount':'Enter Total Ammount',
			'note':'Enter Note',
			'status':'Status',
			'is_paid':'Is Paid',
			'date':'Enter Date',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'ammount': widgets.TextInput(attrs={'placeholder':'Total Ammount', 'class': 'form-control'}),
			'note': widgets.TextInput(attrs={'placeholder':'Note', 'class': 'form-control'}),
			'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
			'is_paid': widgets.CheckboxInput(),
			'date': widgets.DateInput(attrs={'type':'date', 'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'})
		}