
import pandas as pd
import numpy as np

endereco_dados = 'pasta/funcionarios.csv'


df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

print(df_funcionarios.values)