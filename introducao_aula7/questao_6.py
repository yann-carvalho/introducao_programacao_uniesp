# Intermediário: Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1500,00, o aumento é de 10%. Para salários inferiores ou iguais a R$1500,00, o aumento é de 15%.
salario = float(input('Insira seu salário: '))

if salario > 1500.00:
    print(f'Seu aumento foi de 10% e seu novo salário é {(salario * 0.15) + salario:.2f}')
else:
    print(f'Seu aumento foi de 15% e seu novo salário é {(salario * 0.10) + salario:.2f}')