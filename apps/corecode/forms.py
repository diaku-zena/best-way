from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import (
    AcademicSession,
    AcademicTerm,
    SiteConfig,
    StudentClass,
    Subject,
    PermitDocCategory,
    Citizenship,
    DocumentType,
)

SiteConfigForm = modelformset_factory(
    SiteConfig,
    fields=(
        "key",
        "value",
    ),
    extra=0,
)


class AcademicSessionForm(ModelForm):
    prefix = "Academic Session"

    class Meta:
        model = AcademicSession
        fields = ["name", "current"]


class AcademicTermForm(ModelForm):
    prefix = "Academic Term"

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]


class SubjectForm(ModelForm):
    prefix = "Subject"

    class Meta:
        model = Subject
        fields = ["name"]


class StudentClassForm(ModelForm):
    prefix = "Class"

    class Meta:
        model = StudentClass
        fields = ["nome"]

class PermitDocCategoryForm(ModelForm):
    prefix = "PermitDocCategory"

    class Meta:
        model = PermitDocCategory
        fields = ["name"]

class CitizenshipForm(ModelForm):
    prefix = "Citizenship"

    class Meta:
        model = Citizenship
        fields = ["name"]

class DocumentTypeForm(ModelForm):
    prefix = "DocumentType"

    class Meta:
        model = DocumentType
        fields = ["name"]

class CurrentSessionForm(forms.Form):
    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
    )


class FuncaoChefiaForm(ModelForm):
    prefix = "FuncaoChefia"

    class Meta:
        model = StudentClass
        fields = ["nome"]
        


class DepartamentoForm(ModelForm):
    prefix = "Departamento"

    class Meta:
        model = StudentClass
        fields = ["nome"]


class CategoriaForm(ModelForm):
    prefix = "Categoria"

    class Meta:
        model = StudentClass
        fields = ["nome"]

from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()


