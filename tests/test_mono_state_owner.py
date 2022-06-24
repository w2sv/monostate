import pytest

from monostate import MonoState


_INITIAL_A = 0
_INITIAL_B = 1


class MonoStateImplementation(MonoState):
    def __init__(self, a=_INITIAL_A, b=_INITIAL_B):
        super().__init__()

        self.a = a
        self.b = b


@pytest.fixture
def instance() -> MonoStateImplementation:
    MonoStateImplementation()
    return MonoStateImplementation.instance()


def test_initialization(instance):
    assert instance.a == _INITIAL_A
    assert instance.b == _INITIAL_B


def test_value_mirroring_across_instances(instance):
    A_VALUE, B_VALUE = 99, 111

    instance.a, instance.b = A_VALUE, B_VALUE

    new_instance = MonoStateImplementation.instance()
    assert new_instance.a == A_VALUE
    assert new_instance.b == B_VALUE


def test_value_mirroring_on_reinitialization(instance):
    instance.a, instance.b = 12, 13

    reinitialized = MonoStateImplementation()
    assert reinitialized.a == _INITIAL_A
    assert reinitialized.b == _INITIAL_B

    assert instance.a == _INITIAL_A
    assert instance.b == _INITIAL_B


def test_raising_on_missing_initialization():
    class DifferentMonoStateImplementation(MonoState):
        def __init__(self, a):
            super().__init__()

            self.a = a

    with pytest.raises(AttributeError):
        DifferentMonoStateImplementation.instance()


def test_independence_of_different_monostate_owner_implementations(instance):
    class OtherMonoStateImplementation(MonoState):
        def __init__(self, c):
            super().__init__()

            self.c = c

    OtherMonoStateImplementation(9)

    other_instance = OtherMonoStateImplementation.instance()
    assert other_instance.__dict__ == {'c': 9}

    assert instance.a == _INITIAL_A
    assert instance.b == _INITIAL_B
    assert instance.__dict__ == {'a': _INITIAL_A, 'b': _INITIAL_B}

    instance.d = None
    assert hasattr(instance, 'd')
    assert not hasattr(other_instance, 'd')


def test_receiver():

    @MonoStateImplementation.receiver
    def someFunc(a, b, mono_state_instance):
        assert isinstance(mono_state_instance, MonoStateImplementation)
        
    someFunc(3, 4)