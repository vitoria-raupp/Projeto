from django.core.exceptions import ValidationError
import re

def validate_senha(senha):
    if len(senha) < 8:
        raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
    if not re.search(r'\d.*\d', senha):
        raise ValidationError('A senha deve conter pelo menos 2 números.')
    if not re.search(r'[a-zA-Z].*[a-zA-Z]', senha):
        raise ValidationError('A senha deve conter pelo menos 2 letras.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        raise ValidationError('A senha deve conter pelo menos 1 caractere especial.')
