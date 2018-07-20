from django import forms

from .models import Address


class AddressForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    address1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address Line 1'}))
    address2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address Line 2'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    pincode = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Pincode'}))

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

    def clean_name(self):
        return self.cleaned_data['name']

    def save(self, request):
        save_address = Address.objects.create(
            user=request.user,
            name=self.cleaned_data['name'],
            addressLine1=self.cleaned_data['address1'],
            addressLine2=self.cleaned_data['address2'],
            state=self.cleaned_data['state'],
            city=self.cleaned_data['city'],
            pincode=self.cleaned_data['pincode']
        )

    class Meta:
        fields = ['address1', 'address2', 'state', 'pincode', ]
