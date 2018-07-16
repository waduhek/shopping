from django import forms


class Address(forms.Form):
    address1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address Line 1'}))
    address2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address Line 2'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    pincode = forms.DecimalField(max_digits=7, decimal_places=0)

    def clean_address1(self):
        return self.cleaned_data['address1']

    def clean_address2(self):
        return self.cleaned_data['address2']

    def clean_state(self):
        return self.cleaned_data['state']

    def clean_city(self):
        return self.cleaned_data['city']

    def clean_pincode(self):
        return self.cleaned_data['pincode']

    class Meta:
        fields = ['address1', 'address2', 'state', 'pincode', ]
