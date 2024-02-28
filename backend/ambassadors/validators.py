from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_domain(value: str) -> None:
    '''Функция-валидатор для проверки почтового домена.'''
    error_msg = 'Используйте почту Яндекса'
    email_validator = EmailValidator(message=error_msg)
    email_validator(value)

    if not value.lower().endswith('@yandex.ru', 'ya.ru'):
        raise ValidationError(error_msg)
