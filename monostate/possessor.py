import abc
from typing import Dict


class MonoStatePossessor(abc.ABC):
    """ Interface for classes predestined to possess one singular global state, implemented
        by means of the Borg-pattern """

    __mono_state: Dict = {}

    @classmethod
    def __equate_with_mono_state(cls, instance):
        instance.__dict__ = cls.__mono_state

    def __init__(self):
        """ Equate instance dict and global state """

        self.__equate_with_mono_state(self)

    @classmethod
    def instance(cls):
        # create empty instance of subclass
        instance = cls.__new__(cls)
        cls.__equate_with_mono_state(instance)

        return instance