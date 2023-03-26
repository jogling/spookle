from django import forms
from .models import Encounter, Ghost

class EncounterForm(forms.ModelForm):

    existing_ghost = forms.ModelChoiceField(queryset=Ghost.objects.all(), required=False)
    new_ghost = forms.CharField(required=False)

    class Meta:
        model = Encounter
        fields = ['title', 'description', 'existing_ghost', 'new_ghost']  # Add any additional fields as needed

