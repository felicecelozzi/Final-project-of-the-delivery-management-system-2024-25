from django import forms
from .models import Ordine, Corriere, Mezzo

class OrdineForm(forms.ModelForm):
    class Meta:
        model = Ordine
        fields = '__all__'
        def create (self, commit=True):
            ordine = super().create(commit=False)
            if commit:
                ordine.save()
            return ordine

class CorriereForm(forms.ModelForm):
    class Meta:
        model = Corriere
        fields = '__all__'
        def create (self, commit=True):
            corriere = super().create(commit=False)
            if commit:
                corriere.save()
            return corriere

class MezzoForm(forms.ModelForm):
    class Meta:
        model = Mezzo
        fields = '__all__'
        def create (self, commit=True):
            mezzo = super().create(commit=False)
            if commit:
                mezzo.save()
            return mezzo