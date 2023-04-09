num = int(input('Digite um número de 1 a 10: '))

print(f'Tabuada do {num}: ')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')