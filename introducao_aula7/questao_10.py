# Intermediário: Escreva um programa que leia uma lista de nomes e remova todos os nomes duplicados, deixando apenas um de cada nome na lista final.
lista = ['Ana', 'Ana', 'Carolina', 'Yann', 'Yann', 'Ygor']
print('A lista original é', lista)
print('A lista corrigida é', sorted(set(lista)))