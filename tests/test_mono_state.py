import pytest

from monostate import MonoState


_INITIAL_A = 0
_INITIAL_B = 1


class MonoStateImplementation(MonoState):
    def __init__(self, a=_INITIAL_A, b=_INITIAL_B):
        super().__init__(instance_kwarg_name='implementation_instance')

        self.a = a
        self.b = b


@pytest.fixture
def instance() -> MonoStateImplementation:
    MonoStateImplementation()
    return MonoStateImplementation.instance()


def test_initialization(instance):
    assert instance.a == _INITIAL_A
    assert instance.b == _INITIAL_B


def test_is_initialized():
    class SomeMono(MonoState):
        pass

    assert not SomeMono.is_initialized()
    SomeMono()
    assert SomeMono.is_initialized()


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
    assert other_instance.__dict__ == {'c': 9, '_MonoState__instance_kwarg_name': 'monostate_instance'}

    assert instance.a == _INITIAL_A
    assert instance.b == _INITIAL_B
    assert instance.__dict__ == {'a': _INITIAL_A, 'b': _INITIAL_B, '_MonoState__instance_kwarg_name': 'implementation_instance'}

    instance.d = None
    assert hasattr(instance, 'd')
    assert not hasattr(other_instance, 'd')


def test_receiver():
    @MonoStateImplementation.receiver
    def some_func(a, b, implementation_instance):
        assert isinstance(implementation_instance, MonoStateImplementation)
        
    some_func(3, 4)

    @MonoStateImplementation.receiver
    def some_func(monostate_instance):
        pass

    with pytest.raises(TypeError):
        some_func()