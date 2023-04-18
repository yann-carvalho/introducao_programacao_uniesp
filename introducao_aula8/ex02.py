# Lista de frutas
frutas = ['pêra', 'uva', 'maçã', 'kiwi']
# Imprimindo a lista
print(frutas)
# Alterando o elemento que está na posição 1
frutas[1] = 'abacate'
# Imprimindo a lista
print(frutas)
# Adicionando elemento à lista
frutas.insert(2, 'morango')
# Imprimindo a lista
print(frutas)
# Adicionando elemento à lista
frutas.insert(5, 'chuchu') # chuchu não é fruta
# Imprimindo a lista
print(frutas)
# Deletando elemento da lista
del frutas[5]
# Imprimindo a lista
print(frutas)
# Adicionando elemento à lista
frutas.insert(5, 'melancia')
# Imprimindo a lista
print(frutas)
# Descobrindo o índice do elemento
del frutas[frutas.index('melancia')]
# Imprimindo a lista
print(frutas)
# Removendo usando 'remove'
frutas.remove('kiwi')
# Imprimindo a lista
print(frutas)
# Adicionando item à lista
frutas.insert(10, 'ameixa')
# Imprimindo a lista
print(frutas)
# Removendo usando 'pop'
pop_fruta = frutas.pop(frutas.index('ameixa'))
print(f'Pop fruta é {pop_fruta}')
# Imprimindo a lista
print(frutas)