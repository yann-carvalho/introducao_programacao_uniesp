matriz_5x5 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

for lista in matriz_5x5:
    for item in lista:
        if (item % 2) == 0:
            print(f'Este número é par - {item}')
        else:
            print(f'Este número é ímpar - {item}')