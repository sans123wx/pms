from django import template
from ..fnc import decrypt

register = template.Library()
@register.filter(name = 'decrypt_tag')
def decrypt_tag(value , arg):
    if value:
        try:
            decrypt_value = decrypt(value , arg)
        except:
            decrypt_value = value
    else:
        decrypt_value = 'unknown'
    return decrypt_value