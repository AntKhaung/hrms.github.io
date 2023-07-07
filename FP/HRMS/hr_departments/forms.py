from django import forms
from django.forms import widgets
from .models import DepartmentModel

STATUS_CHOICES =(
    ('draft', 'draft'),
    ('Confirm', 'confirm'),
    ('Cancel', 'cancel')
)

class DepartmentForm(forms.ModelForm):
    
    class Meta:
        model = DepartmentModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name', 
            'sequence':'Enter Sequence',  
            'meeting_date':'Enter Meeting Date',
            'total_employees':'Enter Total Employees', 
            'note':'Internal Note', 
            'status':'Status', 
            'is_active':'Is Active', 
            'create_date':'Enter Create Date', 
            'attachment':'Upload Attachment'
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Department Name','class': 'form-control'}),
            'sequence': widgets.NumberInput(attrs={'placeholder':'0','class': 'form-control'}),
            'meeting_date': widgets.DateInput(attrs={'placeholder':'Meeting Date', 'type': 'date','class': 'form-control'}),
            'total_employees': widgets.TextInput(attrs={'placeholder':'Total Employees','class': 'form-control'}),
            'note': widgets.TextInput(attrs={'placeholder':'Internal Note','class': 'form-control'}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'is_active': widgets.CheckboxInput(),
            'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local','class': 'form-control'}),
            'attachment': widgets.ClearableFileInput()
        }