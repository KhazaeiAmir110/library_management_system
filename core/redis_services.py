from threading import Lock
from django.conf import settings
from redis import Redis
from core.structs import UniqueSingletonMeta


class RedisSingletonMeta(UniqueSingletonMeta):
    _instance = None
    _lock = Lock()


class RedisClient(metaclass=RedisSingletonMeta):
    def __init__(self, *args, **kwargs):
        self._client = Redis(settings.REDIS_HOST, settings.REDIS_PORT)

    @property
    def client(self):
        return self._client


redis_client = RedisClient().client


def make_key(key, header=None):
    formatted_key = '{header}_{key}'
    if header is None:
        formatted_key = '{key}'

    return formatted_key.format(header=header, key=key)


def get(key, **options):
    return redis_client.get(key)


def set(key, value, **options):
    options.pop('ex', None)
    redis_client.set(key, value, ex=options.pop('expire', None), **options)


def delete(*key, **options):
    redis_client.delete(*key)
