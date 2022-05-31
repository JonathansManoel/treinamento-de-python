"""
Funções aninhadas.

Funções dentro de funções.
"""

from difflib import ndiff
from typing import List, NoReturn


def file_diff(file_1: str, file_2: str) -> NoReturn:
    def read_file(file: str) -> List:
        return [
            e.replace(',', '')
            for e in open(file).readlines()[1:-1]
        ]

    content_1 = read_file(file_1)
    content_2 = read_file(file_2)

    print(''.join(ndiff(content_1, content_2)))
