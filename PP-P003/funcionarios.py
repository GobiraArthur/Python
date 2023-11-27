class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento, rg, ano_admissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.ano_admissao = ano_admissao
        self.salario = salario

    def __str__(self):
        return f"{self.data_nascimento},{self.nome} {self.sobrenome},{self.salario}\n"

def carregar_funcionarios(arquivo):
    funcionarios = []
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                if len(dados) == 3:  
                    data_nascimento, nome_completo, salario = dados
                    nome_sobrenome = nome_completo.split(' ')
                    if len(nome_sobrenome) >= 2:  
                        nome = nome_sobrenome[0]
                        sobrenome = ' '.join(nome_sobrenome[1:])
                        funcionario = Funcionario(nome, sobrenome, data_nascimento, "", "", salario)
                        funcionarios.append(funcionario)
                    else:
                        print(f"Erro: Linha com dados incompletos: {linha}")
                else:
                    print(f"Erro: Formato de dados inválido na linha: {linha}")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado. Será criado um novo arquivo ao salvar os dados.")

    return funcionarios

def salvar_funcionarios(funcionarios, arquivo):
    with open(arquivo, 'w') as file:
        for funcionario in funcionarios:
            nome_completo = f"{funcionario.nome} {funcionario.sobrenome}"
            file.write(f"{funcionario.data_nascimento},{nome_completo},{funcionario.salario}\n")

def reajusta_dez_porcento(funcionarios):
    for funcionario in funcionarios:
        funcionario.salario = float(funcionario.salario.replace("R$", "").replace(".", "").replace(",", ".")) * 1.1
        funcionario.salario = f"R$ {funcionario.salario:.2f}"

def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    data_nascimento = input("Digite a data de nascimento do funcionário (dia/mês/ano): ")
    rg = input("Digite o RG do funcionário: ")
    ano_admissao = input("Digite o ano de admissão do funcionário: ")
    salario = input("Digite o salário do funcionário (R$ XXXX,XX): ")

    return Funcionario(nome, sobrenome, data_nascimento, rg, ano_admissao, salario)

def excluir_funcionario(funcionarios):
    if not funcionarios:
        print("Não há funcionários para excluir.")
        return funcionarios

    print("Funcionários:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}. {funcionario.nome} {funcionario.sobrenome}")

    try:
        indice = int(input("Digite o número do funcionário a ser excluído: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("Funcionário excluído com sucesso!")
        else:
            print("Número de funcionário inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

    return funcionarios
def main():
    arquivo = 'funcionarios.txt'
    lista_funcionarios = carregar_funcionarios(arquivo)

    while True:
        print("\nMenu:")
        print("1. Adicionar novo funcionário")
        print("2. Reajustar salários em 10%")
        print("3. Excluir funcionário")
        print("4. Mostrar funcionários")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_funcionario = adicionar_funcionario()
            lista_funcionarios.append(novo_funcionario)
            salvar = input("Deseja salvar os dados? (S/N): ")
            if salvar.lower() == "s":
                salvar_funcionarios(lista_funcionarios, arquivo)
                print("Funcionário adicionado e dados salvos com sucesso!")
            else:
                print("Funcionário adicionado.")
        elif opcao == "2":
            reajusta_dez_porcento(lista_funcionarios)
            salvar_funcionarios(lista_funcionarios, arquivo)
            print("Salários reajustados em 10%. Dados salvos.")
        elif opcao == "3":
            lista_funcionarios = excluir_funcionario(lista_funcionarios)
            salvar_funcionarios(lista_funcionarios, arquivo)
        elif opcao == "4":
            print("Funcionários:")
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()