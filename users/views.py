from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.method == "GET":
        context = {
            'forms': LoginForm
        }

        return render(request, 'users/login.html', context=context)

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return render('/products/')
            else:
                form.add_error('username', 'bad_request')

        return render(request, 'users/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('/products/')


def register_view(request):
    if request.method == "GET":
        context = {
            'forms': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password')
                )
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('password2', "stupid!")

        return render(request, 'users/register.html', context={
            'form': form
        })

