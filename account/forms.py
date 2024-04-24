from django import forms


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
        "placeholder" : "Password",
        "required" : True}))
   
