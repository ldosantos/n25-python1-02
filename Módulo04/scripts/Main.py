"""

Programa principal
Author: Luiz Donizeti dos Santos Junior
Version: 2025-04-03
"""

import funcoes
from click import clear #importando somente a função clear
import csv_teste
clear()
funcoes.cabecalho (colunas=50,titulo="Bem Vindo")
funcoes.cabecalho("Boa noite Augusto! tudo bem?", 30)   ## cuidado por que sempre quando importamos uma biblioteca e tiver a funcao chamada ele vai realizar tudo.
funcoes.cabecalho ()
funcoes.cabecalho (colunas=15)
print("fatorial de 5 =", funcoes.fatorial (5))
print("Fatorial de 5= ",funcoes.fatorial_rec(5))
print(csv_teste.coluna_salario*funcoes.fatorial(5))