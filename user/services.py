from rest_framework.exceptions import NotFound

from user.models import User


def create_user(**kwargs):
    return User.objects.create(**kwargs)


def get_user(raise_exception=False, **kwargs):

    user = User.objects.filter(**kwargs).first()
    if not user and raise_exception:
        raise NotFound('user notfound!!!')

    return user
