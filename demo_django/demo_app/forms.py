from django import forms
from .models import Fermier

class FermierForm(forms.ModelForm):
    class Meta:
        model = Fermier
        fields = ['prenom', 'nom']