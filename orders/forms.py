from django import forms
from .models import Order
from django.forms.widgets import HiddenInput


class OrderCreateForm(forms.ModelForm):
    street = forms.CharField(label='Улица', required=False)
    house_number = forms.IntegerField(min_value=1, required=True, label='Номер дома')
    building_number = forms.IntegerField(min_value=1, label='Корпус', required=False)
    apartment = forms.IntegerField(min_value=1, label='Квартира', required=False)

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'city', 'street',
            'house_number', 'building_number', 'apartment', 'address',
        ]
        widgets = {'address': HiddenInput()}

    def clean(self):
        street = str(self.cleaned_data.get('street'))
        house_number = str(self.cleaned_data.get('house_number'))
        building_number = str(self.cleaned_data.get('building_number'))
        apartment = str(self.cleaned_data.get('apartment'))
        address = [street, house_number, building_number, apartment]
        self.cleaned_data['address'] = ', '.join(address)
        return self.cleaned_data
