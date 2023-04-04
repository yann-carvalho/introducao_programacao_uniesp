num = int(input('Forneça um número: '))

# Verifica se o número é maior que 1
if num > 1:
    # Verifica se o número é divisível por outro número além de 1 e ele mesmo
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'não é um número primo')
            break
    else:
        print(num, 'é um número primo')
else:
    print(num, 'não é um número primo')