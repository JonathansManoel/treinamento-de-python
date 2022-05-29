"""Anotações de tipo.

- PEP484: https://www.python.org/dev/peps/pep-0484/
- mypy
- monkeytype
"""


from numbers import Number


def soma(x: int, y: int) -> int:
    return x + y
# soma(1, 2)


def soma2(x: Number, y: Number) -> Number:
    return x + y
# soma2(1, 2.5)


from typing import Union, Any, List, Dict, Sequence, Text

Somavel = Union[Number, str, list]


def soma3(x: Somavel, y: Somavel) -> Somavel:
    return x + y
# soma3(1, 2)


def identidade(val: Any) -> Any:
    return val
# identidade(5441023)


def meu_sum(l: List[Number]) -> Number:
    return sum(l)
# meu_sum([1, 2, 3])


def cadastro_usuario(
    nome: str,
    idade: int,
    gostos: List[str]
    ) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos
        }
# cadastro_usuario('João', 25, ['Python', 'C'])



def meu_min(seq: Sequence):
    return min(seq)
# meu_min([1, 2, 3])
# meu_min((1, 2, 3))
# meu_min({1, 2, 3})




def converte_para_reais(valor: Text):
    ...
# converte_para_reais('')
