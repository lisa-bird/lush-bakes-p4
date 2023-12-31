from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'street_address1', 'street_address2',
                  'county', 'postcode', 'phone_number',)
        widgets = {        
            'email': forms.EmailInput(attrs={'maxlength': 50}),
        }

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
            'postcode': 'Postcode',
            'phone_number': 'Phone Number',            
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
