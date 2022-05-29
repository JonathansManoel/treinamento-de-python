"""Funções como objeto de primeira classe."""
from typing import Callable, Dict
from numbers import Number
func = lambda: 'resultado da função'



calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}
# calc['soma'](1, 2)
# calc['sub'](1, 2)
# calc['mult'](1, 2)
# calc['div'](1, 2)


def soma(x: Number, y: Number) -> Number:
    """Soma dois números."""
    return x + y


def sub(x: Number, y: Number) -> Number:
    """Subtrai dois números."""
    return x - y


def mult(x: Number, y: Number) -> Number:
    """Multiplica dois números."""
    return x * y


def div(x: Number, y: Number) -> Number:
    """Divide dois números."""
    return x / y

calc_nomeado = {
    """
    Soma dois números.
    :param x: Primeiro número.
    :param y: Segundo número.
    :returns: Soma dos dois números.
    """
    'soma': soma,
    """
    Subtrai dois números.
    :param x: Primeiro número.
    :param y: Segundo número.
    :returns: Subtração dos dois números.
    """
    'sub': sub,
    """
    Multiplica dois números.
    :param x: Primeiro número.
    :param y: Segundo número.
    :returns: Multiplicação dos dois números.
    """
    'mult': mult,
    """
    Divide dois números.
    :param x: Primeiro número.
    :param y: Segundo número.
    :returns: Divisão dos dois números.
    """
    'div': div,
}
# calc_nomeado['soma'](1, 2)
# calc_nomeado['sub'](1, 2)
# calc_nomeado['mult'](1, 2)
# calc_nomeado['div'](1, 2)


somas = [
    lambda x: x + 0,
    lambda x: x + 1,
    lambda x: x + 2
    ]
# somas[0](1)
# somas[1](1)
# somas[2](1)


def soma_1(x: Number) -> Number:
    """Soma 1 a qualquer x de entrada."""
    return x + 1
# soma_1(1)
