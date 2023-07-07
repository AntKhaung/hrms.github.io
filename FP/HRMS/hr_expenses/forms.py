from django import forms
from hr_expenses import models
from django.forms import widgets

PAID_BY_CHOICES =(
	('Employee', 'Employee'),
	('Company', 'Company'),
	('Myself', 'Myself')
)

class ExpenseForm(forms.ModelForm):

	class Meta:
		model = models.ExpenseModel
		fields = "__all__"
		labels = {
			'description':'Enter Description',
			'product':'Enter Products',
			'expense_date':'Enter Expense Date',
			'note':'Enter Note',
			'total_ammount':'Total Ammount',
			'paid_by':'Paid By',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'description': widgets.TextInput(attrs={'placeholder':'Eg. Dinner With Customers', 'class': 'form-control'}),
			'product': widgets.TextInput(attrs={'placeholder':'Products', 'class': 'form-control'}),
			'expense_date': widgets.DateInput(attrs={'placeholder':'Expense Date', 'type': 'date', 'class': 'form-control'}),
			'note': widgets.TextInput(attrs={'placeholder':'Note', 'class': 'form-control'}),
			'total_ammount': widgets.TextInput(attrs={'placeholder':'Total Ammount', 'class': 'form-control'}),
			'paid_by': widgets.Select(choices=PAID_BY_CHOICES, attrs={'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
		}