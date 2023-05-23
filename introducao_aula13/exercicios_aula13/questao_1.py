def conta_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in string:
        if letra in vogais:
            contador += 1
    
    return contador
texto = str(input('Digite uma palavra: '))
resultado = conta_vogais(texto)
print(resultado)