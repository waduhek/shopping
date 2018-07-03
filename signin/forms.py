from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUp(forms.Form):
    username = forms.CharField(min_length = 6, max_length = 50, widget = forms.TextInput(attrs = {'placeholder': 'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'E-mail'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}))
    conf_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'First Name'}))
    last_name = forms.CharField(required = False, widget = forms.TextInput(attrs = {'placeholder': 'Last Name (Optional)'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username = username)

        if r.count():
            raise ValidationError('Entered username already exists.')

        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email = email)

        if r.count():
            raise ValidationError('Entered E-mail address already exists.')

        return email

    def clean_conf_password(self):
        password = self.cleaned_data['password']
        conf_password = self.cleaned_data['conf_password']

        if password != conf_password:
            raise ValidationError('Entered passwords do not match.')

        return conf_password

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    def save(self):
        user = User.objects.create_user(
                username = self.cleaned_data['username'],
                email = self.cleaned_data['email'],
                password = self.cleaned_data['password'],
                first_name = self.cleaned_data['first_name'],
                last_name = self.cleaned_data['last_name']
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'conf_password', 'first_name', 'last_name', ]

class SignIn(forms.Form):
    username = forms.CharField(label = 'Username', min_length = 6, max_length = 50)
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

    def clean_username(self):
        return self.cleaned_data['username']

    def clean_password(self):
        return self.cleaned_data['password']

    class Meta:
        model = User
        fields = ['username', 'password', ]