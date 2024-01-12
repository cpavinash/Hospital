from django import forms
from.models import Login,Patient

class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
        widgets={

        }




class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        widgets={

        }