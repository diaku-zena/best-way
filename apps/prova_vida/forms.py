from django import forms
from django.forms import ModelForm
import hrm_app.settings as sett
from django.db import models

from .models import (
    ProvaVida
)


class PrivaVidaForm(ModelForm):
    prefix = "ProvaVida"
    # date_of_birth = DateTimeField(input_formats=sett.DATE_INPUT_FORMATS)
    class Meta:
        model = ProvaVida
        fields = "__all__"

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()