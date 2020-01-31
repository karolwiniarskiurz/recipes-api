from django import forms
from django.forms import Textarea

from domain.models import Recipe, Photo


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)


class RecipeForm(forms.ModelForm):
    photos = forms.CharField(label='Zdjęcia', widget=Textarea(attrs={'rows': 3, 'placeholder': 'Linki do zdjęć oddzielone przecinkiem'}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'main_image', 'time_to_make', 'level']

        widgets = {
            'description': Textarea(attrs={'rows': 5}),
            'steps': Textarea(attrs={'rows': 5})
        }

        labels = {
            'name': 'Nazwa',
            'description': 'Opis',
            'steps': 'Przygotowanie',
            'main_image': 'Link do głównego zdjęcia',
            'time_to_make': 'Czas przygotowania',
            'level': 'Poziom trudności'
        }
