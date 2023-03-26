# sightings/forms.py
from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ('title', 'description', 'location', 'date', 'time', 'ghost_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'required': 'required'})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
        self.fields['ghost_type'].widget.attrs.update({'class': 'form-control', 'required': 'required'})
