# Fácil: Crie um programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo.
name = input('Insira seu primeiro nome: ')
age = int(input('Insira sua idade: '))

if age >= 18:
    print(f'{name}, você pode dirigir um veículo.')
else:
    print(f'{name}, você ainda não pode dirigir um veículo.')