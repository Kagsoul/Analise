
#leia antes os # para entender o que eu queria aplicar no programa, obrigador por visualizar bruno seu careca lindo <3

#programa de cadastro de funcionarios com as seguintes informações: somos de salarios antes de excluir o cadastro, visualizar salario, buscar funcionario por cpf e sair
#O programa deve armazenar os dados dos funcionários em um dicionário e gerar um arquivo JSON para cada funcionário cadastrado.
#O programa permite que o analista cadastres e manipula o salario dos funcionarios, visualizar salario, buscar funcionario por cpf e excluir cadastro, entre outras funçoes.
#O programa deve calcular o salário de cada funcionário com base no tempo de empresa. Se o funcionário está na empresa há mais de 12 meses, ele recebe um aumento de X%.
#O programa deve permitir que o analista visualize o salário de um funcionário específico, informando o CPF,Pq Assim não a erro de informação de CPF.
#o programa deve permitir que o analista busca informação do funcionario por cpf, para que ele possa visualizar as informações do funcionario.



import json
from datetime import datetime
import os

class CadastroFuncionario:
    def __init__(self):
        self.funcionarios = {}  # Dicionário para armazenar os funcionários (CPF como chave)
        self.funcionarios_json = {}  # Dicionário para armazenar os funcionários em JSON

    def cadastrar_funcionario(self, cpf):
        funcionario = {}

        funcionario["nome"] = input("Digite o nome do Funcionario: ")

        funcionario["idade"] = input("Digite a idade do Funcionario: ")

        funcionario["telefone"] = input("Digite o telefone: ")

        funcionario["CPF"] = cpf

        funcionario["Data_de_nascimento"] = input("Digite a data de nascimento (DD/MM/AAAA): ")

        funcionario["conta_bancaria"] = input("Qual a conta bancária: ")
        
        funcionario["endereco"] = input("Digite o endereço do Funcionario (Opcional): ")

        print ("Dados da empresa") # Dados da empresa

        funcionario["Entrou_na_empresa_data"] = input("Qual é a data de entrada na empresa deste funcionario (DD/MM/AAAA): ")

        funcionario["email"] = input("Digite o email: ")

        funcionario["dia_de_pagamento"] = input("Digite o dia de pagamento (DD/MM/AAAA): ")

        funcionario["Salario"] = float(input("Digite o salário deste Funcionario: "))




        # Adiciona o funcionário ao dicionário usando o CPF como chave
        self.funcionarios[funcionario["CPF"]] = funcionario

        # Salva os dados do funcionário em um arquivo JSON
        self.gerar_json(funcionario["CPF"])
        print("\nFuncionario cadastrado com sucesso!")

    def imprimir_resultado(self, funcionario):
        print("\nDados do Funcionario:")
        print("Nome: ", funcionario["nome"])
        print("Idade: ", funcionario["idade"])
        print("CPF: ", funcionario["CPF"])
        print("Salario: ", funcionario["Salario"])
        print("Data de nascimento: ", funcionario["Data_de_nascimento"])
        print("Dia de pagamento: ", funcionario["dia_de_pagamento"])
        print("Conta bancaria: ", funcionario["conta_bancaria"])
        print("Endereco: ", funcionario["endereco"])
        print("Telefone: ", funcionario["telefone"])
        print("Email: ", funcionario["email"])
        print("Entrou na empresa: ", funcionario["Entrou_na_empresa_data"])

    def gerar_json(self, cpf):
        if cpf not in self.funcionarios:
            print("\nFuncionário não encontrado.")
            return

        funcionario = self.funcionarios[cpf]
        with open(f'funcionario_{cpf}.json', 'w') as json_file:
            json.dump(funcionario, json_file, indent=4)
        print("\nJson gerado com sucesso!")

    def calcular_salario(self, cpf):
        if cpf not in self.funcionarios:
            print("\nFuncionário não encontrado.")
            return

        funcionario = self.funcionarios[cpf]
        hoje = datetime.now()
        data_entrada = datetime.strptime(funcionario["Entrou_na_empresa_data"], "%d/%m/%Y")
        meses_na_empresa = (hoje.year - data_entrada.year) * 12 + (hoje.month - data_entrada.month)

        if meses_na_empresa > 12:
            aumento = funcionario["Salario"] * 0.1  # Aumento de 10% se o funcionário está na empresa há mais de 12 meses
            salario_final = funcionario["Salario"] + aumento
            print(f"\nO funcionário {funcionario['nome']} está na empresa há mais de 12 meses.")
            print(f"Salário atual: R$ {funcionario['Salario']:.2f}")
            print(f"Aumento de 10%: R$ {aumento:.2f}")
            print(f"Salário final: R$ {salario_final:.2f}")
        else:
            print(f"\nO funcionário {funcionario['nome']} está na empresa há {meses_na_empresa} meses.")
            print(f"Salário final: R$ {funcionario['Salario']:.2f}")

    def ver_salario(self, cpf):
        if cpf not in self.funcionarios:
            print("\nFuncionário não encontrado.")
            return

        print("\nVisualizando salário do funcionário...")
        self.calcular_salario(cpf)  # Chama o método de cálculo do salário

    def excluir_cadastro(self, cpf):
        if cpf not in self.funcionarios:
            print("\nFuncionário não encontrado.")
            return

        print("\nCalculando salário antes de excluir o cadastro...")
        self.calcular_salario(cpf)  # Calcula o salário antes de excluir

        confirmacao = input("\nDeseja excluir o cadastro do funcionario? (s/n): ")
        if confirmacao.lower() == 's':
            del self.funcionarios[cpf]  # Remove o funcionário do dicionário
            # Remove o arquivo JSON correspondente
            if os.path.exists(f'funcionario_{cpf}.json'):
                os.remove(f'funcionario_{cpf}.json')
            print("\nCadastro excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")

    def buscar_por_cpf(self, cpf):
        arquivo_json = f'funcionario_{cpf}.json'

        if os.path.exists(arquivo_json):
            with open(arquivo_json, 'r') as json_file:
                funcionario = json.load(json_file)
                self.imprimir_resultado(funcionario)
        else:
            print("\nFuncionário não encontrado.")


# Exemplo de uso
cadastro = CadastroFuncionario()

while True:
    cpf = input("\nDigite o CPF do funcionário ou Aperte enter para pular: ")
    print("\nEscolha uma opção:")
    print("1 - Cadastrar funcionário")
    print("2 - Ver salário do funcionário")
    print("3 - Excluir cadastro do funcionário")
    print("4 - Buscar funcionário por CPF ")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastro.cadastrar_funcionario(cpf)  # Opção para cadastrar um funcionário
    elif opcao == "2":
        cadastro.ver_salario(cpf)  # Opção para ver o salário
    elif opcao == "3":
        cadastro.excluir_cadastro(cpf)  # Opção para excluir o cadastro 
    elif opcao == "4":
        cadastro.buscar_por_cpf(cpf)  # Opção para buscar funcionário por CPF (puxar do JSON)
    elif opcao == "5":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")