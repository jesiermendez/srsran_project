from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_dni(value):
    if not value.isdigit():
        raise ValidationError(_('El valor %(value)s no es un DNI válido'), params={'value':value},)
    
    number = int(value)
    if number < 11 and number > 11:
        raise ValidationError(_('El valor %(value)s no tiene 12 digitos'), params={'value':value})
    
def validate_only_phone(value):
    if not value.isdigit():
        raise ValidationError(_('El valor %(value)s no es un teléfono válido'), params={'value':value},)
    
    number = int(value)
    if number < 8 and number > 10:
        raise ValidationError(_('El valor %(value)s no tiene los digitos establecidos'), params={'value':value})
