"""HOFs."""
from itertools import takewhile
from typing import Any, Callable

soma_2 = lambda val: val + 2


# Twice
def reaplica(func: Callable, val: Any) -> Any:
    """
    Recebe uma função e um valor e retorna o resultado da função aplicada ao valor.
    """
    return func(
        func(val)
    )
# reaplica(seleciona('soma'), 2)


def seleciona(op: str) -> Callable:
    """Seleciona uma função, usando seu nome."""
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
    }
    return ops[op]
# seleciona('soma')(2, 3) -> 5
# seleciona('sub')(2, 3) -> -1

palavras = ['amar', 'relaxar', 'python', 'curso', 'estudar']
# sorted(palavras, key=lambda string: string[1]) -> ['amar', 'python', 'relaxar', 'estudar', 'curso']
# sorted(palavras) -> ['amar', 'curso', 'estudar', 'python', 'relaxar']
# list(map(lambda val: val*2, palavras)) -> ['amar', 'curso', 'estudar', 'python', 'relaxar']
# list(map(lambda val: val*2, [1, 2, 3,4,5])) -> [2, 4, 6, 8, 10]


# list(filter(lambda x: x[-2:] == 'ar', palavras)) -> ['amar', 'relaxar', 'estudar']
# list(groupby(palavras, key=lambda string: string[-2:])) -> [('ar', ['amar', 'relaxar', 'estudar'])


# reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) -> 15
# reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) -> 120
# reduce(lambda x, y: x / y, [1, 2, 3, 4, 5]) -> 0.2


# sum([1, 2, 3, 4, 5]) -> 15


# list(takewhile(lambda x: x < 5, [1, 2, 3,4, 5, 6])) -> [1, 2, 3, 4]


def take_cond(func, valores):
    """
    Retorna uma lista com os valores até que a função retorne False.
    """
    return list(takewhile(func, valores))
    for val in valores:
        if func(val):
            yield val
        else:
            break
# take_cond(lambda x: x < 5, [1, 2, 3, 4, 5, 6]) -> [1, 2, 3, 4]
# take_cond(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5]
# take_cond(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8]) -> [1, 2, 3, 4, 5, 6]