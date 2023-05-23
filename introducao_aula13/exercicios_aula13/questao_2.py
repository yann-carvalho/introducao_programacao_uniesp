def calcula_fatorial(num):
    fatorial = 1
    for i in range(num, 0, -1):
        contador *= i
    return fatorial
print(calcula_fatorial(int(input('Insira um número inteiro para obter seu fatorial: '))))