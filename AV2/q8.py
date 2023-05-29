import random

numero_secreto = random.randint(1, 10)
print(numero_secreto)
tentativa = int(input("Digite um número entre 1 e 10: "))

if tentativa == numero_secreto:
    print("Parabéns, você acertou!")

else:
    print("Que pena, você errou!")