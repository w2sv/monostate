import abc
from typing import Dict


class MonoStateOwner(abc.ABC):
    """ Base class for classes which are to own one singular global state, implemented
        by means of the Borg-pattern """

    __mono_states: Dict[str, Dict] = {}

    def __init__(self):
        """ Equates instance dict with global state """

        self.__class__.__mono_states.setdefault(self.__class__.__name__, {})
        self.__mono_state_equated(self)

    @classmethod
    def instance(cls):
        try:
            return cls.__mono_state_equated(cls.__new__(cls))
        except KeyError:
            raise AttributeError(f"{cls.__name__} respective mono state hasn't yet been initialized; "
                                 f"Call MonoStateOwner.__init__ before requesting instance")

    @classmethod
    def __mono_state_equated(cls, instance):
        instance.__dict__ = cls.__mono_states[cls.__name__]
        return instance