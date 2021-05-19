from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_num(value):
    if value > 10:
        raise ValidationError(
            _('%(value)s is not between 0 and 10'),
            params={'value': value},
        )