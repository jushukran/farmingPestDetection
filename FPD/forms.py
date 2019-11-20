from django import forms
from django.contrib.auth import get_user_model
from .models import Farm, History


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class' :'form-control',
            'id':'exampleEmails',
            'required':"true",
            'name': "emailadress" ,
            'aria-required':"true"
    }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'examplePasswords',
                'required': "true",
                'name': "passwords",
                'aria-required': "true"
            }
    ))
User = get_user_model()


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={
                'class' :'form-control',
            'id':'exampleEmail',
            'required':"true",
            'name': "emailadress" ,
            'aria-required':"true"
    }))
    name = forms.CharField(widget=forms.TextInput(
            attrs={
                'class' :'form-control',
                'id': 'name',

            'required':"true",
            'name': "name" ,
            'aria-required':"true"
    }))
    phoneNo = forms.IntegerField(widget=forms.NumberInput(
            attrs={
                'class' :'form-control',
                'id': 'pn',
            'required':"true",
            'name': "phoneNo" ,
            'aria-required':"true"
    }))

    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'examplePassword',
                'required': "true",
                'name': "password",
                'aria-required': "true"
            }
    ))
    password2 = forms.CharField( widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'examplePassword1',
                'required': "true",
                'name': "password_confirmation",
                'aria-required': "true"
            }
    ))


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists.")
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match.')
        return data


class FarmRegistration(forms.ModelForm):
    class Meta:
        model = Farm
        exclude = ['owner']

class PestQuery(forms.ModelForm):
    class Meta:
        model = History
        exclude = ['pest','farmer','timestamp','accuracy']