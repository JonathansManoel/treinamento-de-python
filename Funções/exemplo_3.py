"""Des|empacotamento de argumentos."""

# def meu_sum(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
#     print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):


def meu_sum(*args):
    """
    Função que soma os argumentos.
    *args: argumentos não definidos.
    """
    print(args)
    print(type(args))
    return sum(args)
# def meu_sum(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):

def meu_sum2(x, y, *args):
    """
    Função que soma os argumentos.
    x e y são os primeiros argumentos.
    *args: argumentos não definidos.
    """
    print(args)
    print(type(args))
    return x, y, sum(args)
# def meu_sum2(*args, **kwargs):

# def meu_sum2(*args, **kwargs):
def meu_sum2(*grupo_posicional, **grupo_nomeado):
    """
    Empacota os argumentos.
    Função que soma os argumentos.
    *args: argumentos não definidos. Virá uma tupla.
    **kwargs: argumentos definidos. Virá um dicionário.
    """
    print(grupo_posicional, grupo_nomeado)
    print(type(grupo_posicional), type(grupo_nomeado))
    return grupo_posicional, grupo_nomeado


lista = [-1, 2, 3, 4]


def meu_min(a, b, c, d, *args):
    """
    Ou tiraria o *args e colocaria os argumentos na ordem.
    Função que retorna o menor valor.
    Empacota os argumentos.
    """
    return min((a, b, c, d, *args))
# meu_min(*lista)

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

def meu_max(a=0, b=0, c=0, d=0):
    """
    É como se fosse um argumento definido Kwargs.
    Função que retorna o maior valor.
    Empacota os argumentos.
    """
    return max((a, b, c, d))
# meu_max(**dicionario)


l = [1, 2, 3]
d = {'d': 4, 'e': 5}


def meu_mix(a, b, c, d=0, e=0):
    """
    Função que retorna o mix de valores.
    Empacota os argumentos.
    """
    return a, b, c, d, e
# meu_mix(*l, **d)
