from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  fname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            "class": "sign_up_fname",
            "placeholder": "Your First Name"
        }))
  lname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
            "class": "sign_up_lname",
            "placeholder": "Your Last Name"
        }))
  email = forms.EmailField(widget=forms.EmailInput(attrs={
            "class": "sign_up_email",
            "placeholder": "Your Email Address"
        }))

  class Meta:
    model = User
    fields = ["fname", "lname", "email", "username", "password1", "password2"]

  def __init__(self):
    super(SignUpForm,self).__init__()
    self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
    self.field["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Type in your password'})
    self.field["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password'})
