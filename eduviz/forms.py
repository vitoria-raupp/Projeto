from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
        label='Nome'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nome@exemplo.com'}),
        max_length=254,
        label='Endereço de Email'
    )
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crie uma senha'}),
    )
    password2 = forms.CharField(
        label="Confirmação de Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'}),
        strip=False,
        help_text="Digite a mesma senha novamente, para verificação.",
    )

    def validate_password(self, password):
        # Verifica se a senha tem pelo menos 8 caracteres
        if len(password) < 8:
            raise ValidationError(
                _("A senha deve conter pelo menos 8 caracteres."),
                code='password_too_short',
            )
        
        # Verifica se a senha contém pelo menos 2 números
        if not re.search(r'\d.*\d', password):
            raise ValidationError(
                _("A senha deve conter pelo menos 2 números."),
                code='password_no_digits',
            )

        # Verifica se a senha contém pelo menos 2 letras
        if not re.search(r'[a-zA-Z].*[a-zA-Z]', password):
            raise ValidationError(
                _("A senha deve conter pelo menos 2 letras."),
                code='password_no_letters',
            )

        # Verifica se a senha contém pelo menos um caracter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                _("A senha deve conter pelo menos um caracter especial."),
                code='password_no_special_characters',
            )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        self.validate_password(password1)
        return password1

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nome',
            'email': 'Endereço de Email',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
        help_texts = {
            'password1': _("A senha deve conter pelo menos 8 caracteres, incluindo pelo menos 2 números, 2 letras e 1 caracter especial."),
        }
        error_messages = {
            'password1': {
                'password_too_short': _("A senha deve conter pelo menos 8 caracteres."),
                'password_no_digits': _("A senha deve conter pelo menos 2 números."),
                'password_no_letters': _("A senha deve conter pelo menos 2 letras."),
                'password_no_special_characters': _("A senha deve conter pelo menos um caracter especial."),
            },
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Define o username como o email
        if commit:
            user.save()
        return user
