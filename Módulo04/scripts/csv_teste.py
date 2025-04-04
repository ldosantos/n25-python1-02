"""
Archive: Teste_CSV
Author: Luiz Donizeti
Date: 2025-04-03
"""

import pandas as pd
from click import clear
import openpyxl
clear()
df_arquivo = pd.read_csv("C:\\Python\\CSV.csv", encoding="latin-1")
coluna_salario = df_arquivo ['Salario']
df_arquivo['bonus'] = coluna_salario*float(0.1)
print("DataFrame Original: ")
print(df_arquivo)

## transpondo dataframe

df_arquivo = df_arquivo.T
print("\nDataFrame Transposto")
print(df_arquivo)
df_arquivo.to_excel("C:\\Python\\CSV_comBonus3.xlsx", index=False, engine= "openpyxl" )