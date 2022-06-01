from django import forms
from .models import Sensor


class SensorForm(forms.ModelForm):

    class Meta:
        model = Sensor('country', 'city_name', 'sensor_id')
        fields = ['country', 'city_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            # a dictionary of placeholders appearing on form fields
            'country': 'Country',
            'city_name': 'City',
        }
        self.fields['country'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]

    def __str__(self):
        return str(self.sensor_id)