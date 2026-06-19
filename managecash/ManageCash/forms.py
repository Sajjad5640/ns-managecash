from django import forms
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from ManageCash.models import *
class RegistrationForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    pass

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'datetime' : forms.DateTimeInput(
                attrs={
                    'type':'datetime-local'
                }
            )
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'datetime' : forms.DateTimeInput(
                attrs={
                    'type' :'datetime-local'
                }
            )
        }