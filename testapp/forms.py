from django import forms
from testapp.models import Empmobnumbers
class EmpmobnumbersForm(forms.ModelForm):
    class Meta:
        model=Empmobnumbers
        fields="__all__"
