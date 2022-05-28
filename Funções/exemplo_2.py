"""Serie de funções #2."""

anonima = lambda param: param + 2
""" Lambda é uma função anônima.
    É uma função que não tem nome.
    Podemos usar lambda para criar funções anônimas.
    Param é o nome do parametro. """
anonima_plus = lambda param1, param2: param1 + param2


def soma_posicional(x, y):
    """x e y são parametros posicionais"""
    return x + y


def soma_nomeados(x=7, y=7):
    """x e y são parametros nomeados.

    na falta de um valor, o valor padrão é 7.
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_explicitamente_nomeados(*, x=7, y=7):
    """x e y são parametros nomeados.

    * não aceita parametros posicionais.
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_explicitamente_nomeados2(x=7, *, y=7):
    """x e y são parametros nomeados.
    x é parametro posicional, y é parametro nomeado.
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_explicitamente_posicionais(x, y, /):
    """x e y são parametros nomeados.
    / é um parametro opcional.
    """
    print(f'x: {x}, y: {y}')
    return x + y



def soma_tudo_mix(x, y, /, z, *, w):
    """x e y são parametros nomeados.
    / é um parametro opcional.
    * não aceita parametros posicionais.
    """
    print(f'x: {x}, y: {y}, z: {z}, w: {w}')
    return x + y + z + w