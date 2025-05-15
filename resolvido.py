import pandas as pd
import numpy as np

endereco_dados = 'pasta/funcionarios.csv'


df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

print(df_funcionarios.values)

# Criando arrays
salarios = df_funcionarios['Salário'].to_numpy()
idades = df_funcionarios['Idade'].to_numpy()
tempos = df_funcionarios['Tempo'].to_numpy()

# Calculando métricas
media_salario = np.mean(salarios)
maior_salario = np.max(salarios)
menor_salario = np.min(salarios)
nome_maior_salario = df_funcionarios.loc[df_funcionarios['Salário'] == maior_salario, 'Nome'].values[0]

media_idade = np.mean(idades)
maior_idade = np.max(idades)
menor_idade = np.min(idades)
amplitude_idade = maior_idade - menor_idade
nome_mais_velho = df_funcionarios.loc[df_funcionarios['Idade'] == maior_idade, 'Nome'].values[0]
nome_mais_novo = df_funcionarios.loc[df_funcionarios['Idade'] == menor_idade, 'Nome'].values[0]

media_tempo = np.mean(tempos)
maior_tempo = np.max(tempos)
menor_tempo = np.min(tempos)
amplitude_tempo = maior_tempo - menor_tempo
nome_maior_tempo = df_funcionarios.loc[df_funcionarios['Tempo'] == maior_tempo, 'Nome'].values[0]

# Exibindo resultados
print(f'\nMédia salarial: R$ {media_salario:.2f}')
print(f'Maior salário: {nome_maior_salario} (R$ {maior_salario:.2f})')

print(f'\nFuncionário mais velho: {nome_mais_velho} ({maior_idade} anos)')
print(f'Funcionário mais novo: {nome_mais_novo} ({menor_idade} anos)')
print(f'Amplitude de idade: {amplitude_idade} anos')
print(f'Média de idade: {media_idade:.0f} anos')

print(f'\nFuncionário com mais tempo de empresa: {nome_maior_tempo} ({maior_tempo} anos)')
print(f'Menor tempo de empresa: {menor_tempo} anos')
print(f'Amplitude de tempo de empresa: {amplitude_tempo} anos')
print(f'Média de tempo de empresa: {media_tempo:.0f} anos')

print(f'\nTotal de funcionários: {len(df_funcionarios)}')
