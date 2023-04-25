import random

n_colunas = int(input('Digite o número de colunas: '))
n_elementos = int(input('Digite o número de elementos:'))
matriz = []
for i in range(n_colunas):
    lista = []

    for j in range(n_elementos):
        lista.append(random.randint(0,1000))

    matriz.append(lista)

for lista in matriz:
    print(lista)

if ((len(matriz) % 2) == 0) and ((len(matriz[0])% 2) == 0):

    meio_da_matriz = (len(matriz) / 2)
    meio_da_matriz2 = meio_da_matriz + 1

    print(matriz[meio_da_matriz][meio_da_matriz])
    print(matriz[meio_da_matriz2][meio_da_matriz2])