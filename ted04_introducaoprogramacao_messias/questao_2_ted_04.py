# TED 04 - QUESTÃO 2
# Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

apple1 = float(1.30)
apple2 = float(1.00)
compra = float(input("Insira o número de maçãs compradas: "))

if compra >= 12:
    print(f"O valor total da sua compra é R$ {apple2 * compra}")
else:
    print(f"O valor total da sua compra é R$ {apple1 * compra}.")