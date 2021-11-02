import abc
from typing import Dict


class MonoStatePossessor(abc.ABC):
    """ Interface for classes predestined to possess one singular global state, implemented
        by means of the Borg-pattern """

    __mono_state: Dict = {}

    def __init__(self):
        """ Equate instance dict and global state """

        self.__dict__ = self.__mono_state

    @classmethod
    def get_instance(cls):
        # create empty instance of subclass
        instance = cls.__new__(cls)

        # equate instance dict and global state
        super(cls, instance).__init__()

        return instance