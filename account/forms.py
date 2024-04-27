from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "type" : "username",
        "placeholder" : "Username",
        "required" : True}))
      
    password = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        "placeholder" : "Password",
        "required" : True}))



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "type" : "username",
        "placeholder" : "Username",
        "required" : True}))

    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        "type" : "email",
        "placeholder" : "Email Address",
        "required" : True}))

    password1 = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        "placeholder" : "Password",
        "required" : True}))
    
    password2 = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        "placeholder" : "Repeat Password",
        "required" : True}))
   


class Meta:
    model = User
    fields = ["useNme", "email", "password1", "password2"]



    def clean(self):
        password1 = self.cleaned_data("password1")
        password2 = self.cleaned_data("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords are not same")
        
        return password1








