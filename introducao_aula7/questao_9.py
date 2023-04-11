# Intermediário: Faça um programa que gere a tabuada de um número informado pelo usuário.
num = int(input('Insira um número inteiro de 1 a 10: '))

print(f'Tabuada do {num}: ')
for i in range(1, 11):
    tabuada = num * i
    print(f'{num} x {i} = {tabuada}')