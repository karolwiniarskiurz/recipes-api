from django.contrib.auth.models import User


def is_authenticated_headers(headers):
    username = headers.get('HTTP_USERNAME')
    password = headers.get('HTTP_PASSWORD')
    return is_authenticated(username, password)


def is_authenticated(username, password):
    try:
        User.objects.get(username=username, password=password)
        return True
    except User.DoesNotExist:
        return False
