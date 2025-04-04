import datetime as horas

def validar_entrada_monetaria(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                print("Por favor, insira um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def calcular_salario():
    historico = []

    while True:
        nome = input("Digite seu nome: ")
        valor_por_hora = validar_entrada_monetaria(f"Qual o valor da sua hora de trabalho, {nome}? R$")
        horas_extras = validar_entrada_monetaria(f"Quantas horas extras {nome} trabalhou no mês? ")
        valor_hora_extra = validar_entrada_monetaria(f"Qual o valor da hora extra de {nome}? R$")
        dias_trabalho = int(input(f"Quantos dias {nome} trabalhou no mês? "))
        if dias_trabalho < 1 or dias_trabalho > 31:
            print("Número de dias inválido. Considerando 30 dias como padrão.")
            dias_trabalho = 30
        horas_por_dia = 8
        salario_bruto = valor_por_hora * horas_por_dia * dias_trabalho
        salario_bruto += valor_hora_extra * horas_extras
        irrf = 8 / 100
        inss = 5 / 100
        sindicado = validar_entrada_monetaria(f"Quanto {nome} vai pagar para o sindicato? R$")
        valor_irrf = salario_bruto * irrf
        valor_inss = salario_bruto * inss
        print(f"Desconto de IRRF (8%): R${valor_irrf:.2f}")
        print(f"Desconto de INSS (5%): R${valor_inss:.2f}")
        print(f"Desconto do Sindicato: R${sindicado:.2f}")
        vale_transporte = validar_entrada_monetaria("Quanto de vale-transporte será descontado? R$")
        vale_refeicao = validar_entrada_monetaria("Quanto de vale-refeição será descontado? R$")
        salario_liquido = salario_bruto - (valor_irrf + valor_inss + sindicado + vale_transporte + vale_refeicao)
        print(f"Salário Líquido: R${salario_liquido:.2f}")
        historico.append({
            'Nome': nome,
            'Salário Bruto': salario_bruto,
            'IRRF': valor_irrf,
            'INSS': valor_inss,
            'Sindicato': sindicado,
            'Vale-Transporte': vale_transporte,
            'Vale-Refeição': vale_refeicao,
            'Salário Líquido': salario_liquido,
            'Horas Extras': horas_extras,
            'Valor Hora Extra': valor_hora_extra,
            'Data de Cálculo': horas.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
        continuar = input("\nDeseja calcular novamente? (s/n): ")
        if continuar.lower() != 's':
            break
    print("\nHistórico de Cálculos:")
    for item in historico:
        print("\n-----------------------------")
        print(f"Nome: {item['Nome']}")
        print(f"Data de Cálculo: {item['Data de Cálculo']}")
        print(f"Salário Bruto: R${item['Salário Bruto']:.2f}")
        print(f"IRRF (8%): R${item['IRRF']:.2f}")
        print(f"INSS (5%): R${item['INSS']:.2f}")
        print(f"Sindicato: R${item['Sindicato']:.2f}")
        print(f"Vale-Transporte: R${item['Vale-Transporte']:.2f}")
        print(f"Vale-Refeição: R${item['Vale-Refeição']:.2f}")
        print(f"Salário Líquido: R${item['Salário Líquido']:.2f}")
        print(f"Horas Extras: {item['Horas Extras']} horas")
        print(f"Valor Hora Extra: R${item['Valor Hora Extra']:.2f}")

def main():
    data_atual = horas.datetime.now()
    print(f"Data de cálculo: {data_atual.strftime('%d/%m/%Y %H:%M:%S')}")
    calcular_salario()

if __name__ == "__main__":
    main()
