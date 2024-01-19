import random

aleatorio = random.randint(1, 101)
tentativas = 0
palpite = 0
print("Jogo de advinhação")

while tentativas <=8 or palpite == aleatorio:
    palpite = int(input("Qual o seu palpite? "))
    tentativas += 1
    if palpite > aleatorio:
        print("Menos...")
    if palpite < aleatorio:
        print("Mais...")
    if palpite == aleatorio:
        print("Acertou em {} tentativas".format(tentativas))
        break

if palpite != aleatorio:
    print("Perdeu, o número era {}".format(aleatorio))
