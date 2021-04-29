from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.models import ModelForm
from .models import MyUser 
from django.utils.translation import gettext, gettext_lazy as _
from django import forms


class LoginForm(AuthenticationForm):
    
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})

class RegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget())

    class Meta:
        model = MyUser
        fields = ("name", "email", "date_of_birth")
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control input', 'placeholder': field})
        self.fields['email'].widget.attrs.update({'class' : 'form-control input', 'placeholder': 'email'})





    






