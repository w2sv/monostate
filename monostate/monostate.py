import abc
from typing import Dict, Callable, TypeVar, Any, cast
from functools import wraps


FuncT = TypeVar("FuncT", bound=Callable[..., Any])


class MonoState(abc.ABC):
    """ Base class for classes which are to own one singular global state, implemented
        by means of the Borg-pattern """

    __mono_states: Dict[str, Dict] = {}

    def __init__(self, instance_kwarg_name='monostate_instance'):
        """ Equates instance dict with global state """

        self.__class__.__mono_states.setdefault(self.__class__.__name__, {})
        self.__instance_and_mono_state_equated(self)

        self.__instance_kwarg_name = instance_kwarg_name

    @classmethod
    def is_initialized(cls) -> bool:
        return cls.__name__ in cls.__mono_states

    @classmethod
    def instance(cls):
        try:
            return cls.__instance_and_mono_state_equated(cls.__new__(cls))
        except KeyError:
            raise AttributeError(f"{cls.__name__} mono state not yet initialized")

    @classmethod
    def __instance_and_mono_state_equated(cls, instance):
        instance.__dict__ = cls.__mono_states[cls.__name__]
        return instance

    @classmethod
    def receiver(cls, f: FuncT) -> FuncT:
        """ Function decorator, passing subtype instance as trailing kwarg
            'mono_state_instance' to f """
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            instance = cls.instance()
            kwargs.update({instance.__instance_kwarg_name: instance})
            return f(*args, **kwargs)
        return cast(FuncT, wrapper)