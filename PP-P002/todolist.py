#ToDo List

tarefas = []
# Função para listar as tarefas
def listar():
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{idx}.{tarefa['descricao']} {status}")

# Função para registrar as tarefas
def registrar():
    descricao = input("Descreva a nova tarefa: ").capitalize()
    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa registrada!!!")

# Função para marcar uma tarefa como realizada
def marcar():
    listar()
    id = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
    if id <= len(tarefas):
        tarefa = tarefas.pop(id - 1)
        tarefa["concluida"] = True
        tarefas.insert(0, tarefa)
        print("Tarefa marcada como realizada!!!")
    else:
        print("Tarefa não encontrada ou já foi realizada.")

# Função para editar uma tarefa
def editar_tarefa():
    listar()
    id = int(input("Digite o ID da tarefa a ser editada: "))
    if id <= len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[id - 1]["descricao"] = nova_descricao
        print("Tarefa editada com sucesso!!!")
    else:
        print("Tarefa não encontrada.")

# Loop principal do programa
while True:
    
    print("1.Listar tarefas")
    print("2.Registrar nova tarefa")
    print("3.Marcar tarefa como realizada")
    print("4.Editar tarefa")
    print("5.Sair")
    opcao = input("Escolha uma opção: ")



    if opcao == "1":
        listar()
    elif opcao == "2":
        registrar()
    elif opcao == "3":
        marcar()
    elif opcao == "4":
        editar_tarefa()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Escolha novamente.")