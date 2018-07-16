from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from . import forms


def signupView(request):
    if request.method == 'POST':
        signup = forms.SignUp(request.POST)

        if signup.is_valid():
            signup.save()

            username = signup.cleaned_data['username']
            password = signup.cleaned_data['password']

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('shop:home')

    else:
        signup = forms.SignUp()

    return render(request, 'signup.html', {'form': signup})


def signinView(request):
    # logout(request)

    if request.method == 'POST':
        signin = forms.SignIn(request.POST)

        if signin.is_valid():
            username = signin.cleaned_data['username']
            password = signin.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('shop:home')

            else:
                messages.error(request, 'Entered username or password is incorect.')

    else:
        signin = forms.SignIn()

    return render(request, 'signin.html', {'form': signin})


def signoutView(request):
    logout(request)

    return redirect('shop:home')
