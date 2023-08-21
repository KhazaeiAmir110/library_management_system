from abc import abstractmethod
from threading import Lock


class SingletonMetaBase(type):
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls._has_instance() is False:
            with cls._lock:
                if cls._has_instance() is False:
                    instance = super().__call__(*args, **kwargs)
                    cls._register_instance(instance)

        return cls._get_instance()

    @abstractmethod
    def _has_instance(cls):
        raise NotImplementedError()

    @abstractmethod
    def _register_instance(cls, instance):
        raise NotImplementedError()

    @abstractmethod
    def _get_instance(cls):
        raise NotImplementedError()


class UniqueSingletonMeta(SingletonMetaBase):
    _instance = None
    _lock = Lock()

    def _has_instance(cls):
        return cls._instance is not None

    def _register_instance(cls, instance):
        cls._instance = instance

    def _get_instance(cls):
        return cls._instance
