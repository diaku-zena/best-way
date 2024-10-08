from django import forms
from django.forms import ModelForm
import hrm_app.settings as sett
from django.db import models

from .models import (
    Employee
)


class EmployeeForm(ModelForm):
    prefix = "Employee"
    # date_of_birth = DateTimeField(input_formats=sett.DATE_INPUT_FORMATS)
    class Meta:
        model = Employee
        exclude = ["current_status"]


from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()
