import random
import numpy as np

x = int(input('Digite a dimensão x da matriz: '))
y = int(input('Digite a dimensão y da matriz: '))
matriz = []

for i in range(x):
    linha = []
    for j in range(y):
        linha.append(random.randint(0,100))
    matriz.append(linha)
print(matriz)

linhas, colunas = matriz.shape
if linhas % 2 == 1 and colunas % 2 == 1:
    elemento_central = matriz[linhas // 2, colunas // 2]
    print(f'O elemento central é {elemento_central}')
elif linhas % 2 == 0 and colunas % 2 == 0:
    elemento_central1 = matriz[linhas // 2 - 1, colunas // 2 - 1]
    print('Os elementos centrais são: ')
else:
    print('A matriz não tem elemento central')
