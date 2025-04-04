"""
Programa de teste de escopo de variáveis -2
Author: Luiz Donizeti dos Santos Junior
Version: 00 2025-04-03
"""

from click import clear
def calculo ():
    global c, d
    a = 5
    b = a + c  ## 5 + 10
    c = 30
    d = 50
    return b
# Programa Principal
c = 10
print (calculo())
print ("Valor de c= ",  c, "Valor de d=", d)