"""Funções parciais."""

# anterior
def soma_2(x):
    return x + 2

soma_2 = lambda x: x + 2

from operator import add, mul, itemgetter
def soma_2(x):
    return add(x, 2)

soma_2 = lambda x: add(x, 2)

from functools import partial, reduce

soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)


reduce(add, [1, 2, 3, 4, 5]) # Somatório
reduce(mul, [1, 2, 3, 4, 5]) # multiplicação

somatorio = partial(reduce, add)
# somatorio([1, 2, 3, 4, 5]) -> 15

multiplicatorio = partial(reduce, mul)
# multiplicatorio([1, 2, 3, 4, 5]) -> 120

mul_2_all = partial(map, mul_2)
# mul_2_all([1, 2, 3, 4, 5]) -> [2, 4, 6, 8, 10]

ordenar_1 = partial(sorted, key=itemgetter(1))
# ordenar_1(['ab', 'aa', 'ac']) -> ['aa', 'ab', 'ac']


def func(b, c, d, e, database=None):
    return database, b, c, d, e

func_postgress = partial(func, database='postgres')
# func_postgress(1, 2, 3, 4) -> ('postgres', 1, 2, 3, 4)

func_maria = partial(func, database='mariaDB')
# func_maria(1, 2, 3, 4) -> ('mariaDB', 1, 2, 3, 4)

func_mongo = partial(func, database='mongoDB')
# func_mongo(1, 2, 3, 4) -> ('mongoDB', 1, 2, 3, 4)
