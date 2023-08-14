from django import template
register= template.Library()


# using decortor
@register.filter(name='mylower')
def empLower(value):
    result = value[:3].lower()
    return result

# register.filter('mylower',empLower)
