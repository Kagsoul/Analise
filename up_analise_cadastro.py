import json
from datetime import datetime
import re

class CadastroFuncionario:
    def __init__(self, arquivo_base='funcionarios.json'):
        self.arquivo_base = arquivo_base
        self.funcionarios = self.carregar_dados()

    def carregar_dados(self):
        """Carrega os dados existentes do arquivo JSON"""
        try:
            with open(self.arquivo_base, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salvar_dados(self):
        """Salva todos os dados no arquivo JSON principal"""
        with open(self.arquivo_base, 'w') as f:
            json.dump(self.funcionarios, f, indent=4, ensure_ascii=False)

    def validar_cpf(self, cpf):
        """Valida se o CPF tem formato válido"""
        cpf = ''.join(filter(str.isdigit, cpf))
        return len(cpf) == 11 and cpf.isdigit()

    def validar_data(self, data):
        """Valida se a data está no formato DD/MM/AAAA"""
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_email(self, email):
        """Valida formato básico de email"""
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

    def input_validado(self, mensagem, tipo=str, validacao=None):
        """Função auxiliar para input com validação"""
        while True:
            valor = input(mensagem).strip()
            if not valor and tipo == str:  # Campo opcional
                return ""
            try:
                valor_convertido = tipo(valor)
                if validacao and not validacao(valor):
                    print("Formato inválido. Tente novamente.")
                    continue
                return valor_convertido
            except ValueError:
                print(f"Por favor, insira um valor válido ({tipo.__name__}).")

    def cadastrar_funcionario(self, cpf):
        """Cadastra um novo funcionário com validações"""
        if not self.validar_cpf(cpf):
            print("CPF inválido. Deve conter 11 dígitos.")
            return
        if cpf in self.funcionarios:
            print("Funcionário já cadastrado com este CPF.")
            return

        funcionario = {}
        funcionario["nome"] = self.input_validado("Nome do funcionário: ")
        funcionario["idade"] = self.input_validado("Idade: ", int)
        funcionario["telefone"] = self.input_validado("Telefone: ")
        funcionario["CPF"] = cpf
        funcionario["Data_de_nascimento"] = self.input_validado(
            "Data de nascimento (DD/MM/AAAA): ", 
            str, 
            self.validar_data
        )
        funcionario["conta_bancaria"] = self.input_validado("Conta bancária: ")
        funcionario["endereco"] = self.input_validado("Endereço (opcional): ")
        print("Dados da empresa")
        funcionario["Entrou_na_empresa_data"] = self.input_validado(
            "Data de entrada (DD/MM/AAAA): ",
            str,
            self.validar_data
        )
        funcionario["email"] = self.input_validado(
            "Email: ",
            str,
            self.validar_email
        )
        funcionario["dia_de_pagamento"] = self.input_validado(
            "Dia de pagamento (DD/MM/AAAA): ",
            str,
            self.validar_data
        )
        funcionario["Salario"] = self.input_validado("Salário: ", float)

        self.funcionarios[cpf] = funcionario
        self.salvar_dados()
        print("\nFuncionário cadastrado com sucesso!")

    def calcular_diferenca_meses(self, data_entrada):
        """Calcula diferença em meses entre data de entrada e hoje"""
        hoje = datetime.now()
        entrada = datetime.strptime(data_entrada, "%d/%m/%Y")
        return (hoje.year - entrada.year) * 12 + (hoje.month - entrada.month)

    def exibir_funcionario(self, funcionario):
        """Exibe informações do funcionário de forma formatada"""
        print("\nDados do Funcionário:")
        for chave, valor in funcionario.items():
            print(f"{chave.replace('_', ' ').title()}: {valor}")

    def calcular_salario(self, cpf):
        """Calcula salário com possível aumento"""
        funcionario = self.funcionarios.get(cpf)
        if not funcionario:
            print("\nFuncionário não encontrado.")
            return

        meses = self.calcular_diferenca_meses(funcionario["Entrou_na_empresa_data"])
        salario_base = funcionario["Salario"]
        
        if meses > 12:
            aumento = salario_base * 0.1
            salario_final = salario_base + aumento
            print(f"\n{funcionario['nome']} está na empresa há {meses} meses")
            print(f"Salário base: R$ {salario_base:.2f}")
            print(f"Aumento (10%): R$ {aumento:.2f}")
            print(f"Salário final: R$ {salario_final:.2f}")
        else:
            print(f"\n{funcionario['nome']} está na empresa há {meses} meses")
            print(f"Salário: R$ {salario_base:.2f}")

    def excluir_cadastro(self, cpf):
        """Exclui cadastro com confirmação"""
        if cpf not in self.funcionarios:
            print("\nFuncionário não encontrado.")
            return

        self.calcular_salario(cpf)
        if self.input_validado("\nConfirma exclusão? (s/n): ").lower() == 's':
            del self.funcionarios[cpf]
            self.salvar_dados()
            print("\nCadastro excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")

def main():
    cadastro = CadastroFuncionario()
    opcoes = {
        "1": ("Cadastrar funcionário", cadastro.cadastrar_funcionario),
        "2": ("Ver salário", cadastro.calcular_salario),
        "3": ("Excluir cadastro", cadastro.excluir_cadastro),
        "4": ("Buscar funcionário", lambda cpf: cadastro.exibir_funcionario(cadastro.funcionarios.get(cpf, {}))),
        "5": ("Sair", None)
    }

    while True:
        cpf = cadastro.input_validado("\nDigite o CPF (ou Enter para sair): ")
        if not cpf:
            break

        print("\nOpções:")
        for k, v in opcoes.items():
            print(f"{k} - {v[0]}")
        
        opcao = input("Escolha uma opção: ")
        if opcao in opcoes:
            if opcao == "5":
                print("\nSaindo...")
                break
            if not cadastro.validar_cpf(cpf):
                print("CPF inválido!")
                continue
            opcoes[opcao][1](cpf)
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()
