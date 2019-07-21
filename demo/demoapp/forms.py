from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        exclude=('user',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # user.username 	= 	self.clean_username['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user