from django import template


def difficulty_level(value):
    switcher = {
        'VE': 'bardzo łatwe',
        'E': 'łatwe',
        'M': 'średnie',
        'H': 'trudne',
        'VH': 'bardzo trudne'
    }
    return switcher.get(value)


register = template.Library()
register.filter('difficulty_level', difficulty_level)
