lista_produtos = {'codigo': 0, 'nome': '', 'preco': 0}
lista_geral = []


def inserir():
    print("Qual o nome do produto que você deseja adicionar?")
    lista_produtos['nome'] = input().capitalize()
    print("Qual o preço do produto?")
    lista_produtos['preco'] = round(float(input()), 2)
    lista_produtos['codigo'] = str(len(lista_geral)).zfill(13)
    lista_geral.append(dict(lista_produtos))  # Adiciona uma cópia dos produtos à lista_geral

def excluir():
    print("Qual o nome do produto que deseja excluir?")
    nome_excluir = input()
    for x in range(len(lista_geral)):
        if lista_geral[x]['nome'] == nome_excluir:
            del lista_geral[x]
            print("Produto excluído com sucesso!")
            break  # Saia do loop após excluir o produto

def listar():
    # Ordena a lista de produtos pelo preço antes de exibi-la
    lista_g = sorted(lista_geral, key=lambda x: x['preco'])
    

    # Exibe os produtos em blocos de 10
    for i in range(0, len(lista_g), 10):
        print("\nLista de Produtos:")
        for produto in lista_g[i:i+10]:
            print(f"{produto['nome']} - R${produto['preco']:.2f}")

        # Solicita ao usuário se deseja continuar exibindo
        continuar = input("Deseja exibir mais 10 produtos? (s/n): ")
        if continuar.lower() != 's':
            break


   

def consultar():
    print("Qual o código do produto que deseja consultar?")
    codigo_consultar = int(input())
    for produto in lista_geral:
        if int(produto['codigo']) == codigo_consultar:
            print(produto['nome'] + " - R$" + str(produto['preco']))
            break  # Saia do loop após encontrar o produto

def main():
    while True:
        print("O que deseja fazer?")
        print("1 - Inserir")
        print("2 - Excluir")
        print("3 - Listar")
        print("4 - Consultar")
        print("0 - Sair")
        choice = int(input())

        if choice == 1:
            inserir()
        elif choice == 2:
            excluir()
        elif choice == 3:
            listar()
        elif choice == 4:
            consultar()
        elif choice == 0:
            break

if __name__ == '__main__':
    main()