from django import forms
from .models import Users
import re
from django.core.exceptions import ValidationError


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'data', 'placeholder': 'Телефон, имя пользователя или эл. адрес'}),
            'password': forms.TextInput(attrs={'class': 'data', 'type': 'password', 'placeholder': 'Пароль'}),
        }