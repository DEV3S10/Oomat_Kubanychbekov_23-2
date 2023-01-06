from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
