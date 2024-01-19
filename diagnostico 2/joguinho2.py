import random 

print ("Jogo de advinhação")
print ("Vamos jogar!! Pense em um número entre 1 e 100")
acertei = False
tentativas = 1
maior = 101
menor = 1
aleatorio = random.randint(1, 101)
lista = []

while acertei == False:
    lista.append(aleatorio)
    print ("Meu palpite é: " + str(aleatorio))
    print ("O numero que você pensou é maior ou menor que " + str(aleatorio) + "?")
    resposta = int (input("Digite 1 para maior, 2 para menor, 3 para acertou: "))
    if resposta == 1:
        menor = aleatorio
    if resposta == 2:
        maior = aleatorio
    if resposta == 3:
        acertei = True
    aleatorio = (menor + maior) // 2
    print ("eu tentei " + str(tentativas) + " vezes")
    tentativas = tentativas + 1
if acertei == True:
    print ("Parabens para mim, eu acertei! Em " + str(tentativas-1) + " tentativas")
if tentativas > 8:
    x = int(input("Que pena, eu perdi! Qual era o numero?"))
    print ("Você trapacecou ")
