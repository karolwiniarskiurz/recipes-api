from django.contrib.auth.models import User


def get_user_by_username_from_headers(headers):
    try:
        username = headers.get('HTTP_USERNAME')
        return User.objects.get(username=username)
    except User.DoesNotExist:
        raise Exception("Something's fucky")
