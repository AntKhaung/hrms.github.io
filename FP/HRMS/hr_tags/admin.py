from django.contrib import admin

# Register your models here.
from .models import JobTagModel
from .models import EmployeeTagModel
from .models import ContractTagModel
from .models import ResumeTagModel

admin.site.register(JobTagModel)
admin.site.register(EmployeeTagModel)
admin.site.register(ContractTagModel)
admin.site.register(ResumeTagModel)