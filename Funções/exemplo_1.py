"""Serie de funções #1."""

def funcao_nomeada():
    """Função nomeada."""
    return 'oi'

anonima = lambda : 'oi'
"""Função anônima."""

class FuncaoClasse:
    """Função de classe.
    Como a função é chamada, ela é executada.
    self é o objeto que está sendo chamado.
    Metodo __call__ é um método especial.
    Retorna 'oi'.
    """
    def __call__(self):
        return 'oi'