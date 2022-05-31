"""Operator."""

1 + 1
1 - 1
1 * 1
1 / 1
1 // 1
1 % 1
1 ** 1
1 <op> 1

from operator import add , mul, sub, itemgetter

# add(1, 2) -> 3

from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])) -> 15
# print(reduce(add, [1, 2, 3, 4, 5])) -> 15

# print(reduce(lambda x, y: x - y, [1, 2, 3, 4, 5])) -> -8
# print(reduce(sub, [1, 2, 3, 4, 5])) -> -8

# print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])) -> 120
# print(reduce(mul, [1, 2, 3, 4, 5])) -> 120


palavras = ['amar', 'relaxar', 'python', 'curso', 'estudar']

# sorted(palavras, key=lambda string: string[1])
# sorted(palavras, key=itemgetter(1))