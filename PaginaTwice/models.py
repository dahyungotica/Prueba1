from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models

def validate_email_at_symbol(value):
    try:
        validate_email(value)
    except ValidationError as e:
        if '@' not in value:
            raise ValidationError('El correo electrónico debe contener al menos un "@".')

class UsuariosTwice(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo         = models.EmailField(unique=True, validators=[validate_email_at_symbol])

    def __str__(self):
        return self.nombre_usuario

