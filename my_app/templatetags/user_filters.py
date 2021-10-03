from django import template
from django.conf import settings
import datetime

register = template.Library()


@register.filter
def age_validation(birth_date):
    current_date = datetime.date.today()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return 'Allowed' if age > settings.USER_ALLOWED_AGE else 'Blocked'


@register.filter
def bizz_fuzz(number):
    result = ''
    if not number % 3:
        result += 'Bizz'
    if not number % 5:
        result += 'Fuzz'
    return result if result else number
