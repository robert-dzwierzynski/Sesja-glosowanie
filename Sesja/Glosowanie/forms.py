

from .models import Glosowanie, Uchwala
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GlosowanieForm(forms.ModelForm):
    class Meta:
        model = Glosowanie

        exclude = (
            'id_uzytkownika',
            'id_uchwaly',
        )
        widgets = {
            'vote':forms.RadioSelect()
        }

class WszystkieUchwalyForm(forms.ModelForm):
    class Meta:
        model = Uchwala
        exclude = {

        }
        widgets = {
            'is_visible':forms.CheckboxInput()
        }
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )