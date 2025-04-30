turma1 = [10, 20, 20, 30, 40]
turma2 = [5, 10, 15]

def calcular_variancia(valores):
    n = len(valores)
    media = sum(valores) / n
    variancia = sum((x - media) ** 2 for x in valores) / n
    return variancia

variancia_turma1 = calcular_variancia(turma1)
variancia_turma2 = calcular_variancia(turma2)

print(f"Variância da Turma 1: {variancia_turma1:.3f}")
print(f"Variância da Turma 2: {variancia_turma2:.3f}")

media_values = [13, 3, 45, 26, 27, 50, 63, 81, 76, 52, 86, 92, 98]

def valores_maior(maior):
    i = len(maior)
    media_value = sum(maior) / i
    soma = sum((x - media_value) ** 2 for x in maior) / i
    return soma

valores_media = valores_maior(media_values)


print(f"\nVariancia dos valores na lista 'media': {valores_media:.1f}")

resposta = input("Essa medida é ideal para representar o seu desempenho? (Sim/Nao):\n ")
print(f"Você respondeu: {resposta}")
resposta = input (f'{resposta} justifica sua resposta?\n')

calcular_variancia()
valores_maior()