from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [
            'name',
            'type',
            'location',
            'price',
            'price_unit',
            'photo'
        ]
        widgets = {'location': LeafletWidget()}