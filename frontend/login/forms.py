from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label="Email",max_length=100)
	password = forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput)
class RegisterForm(forms.Form):
	name=forms.CharField(label="Name",max_length=100)
	email = forms.EmailField(label="Email",max_length=100)
	password=forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput)
