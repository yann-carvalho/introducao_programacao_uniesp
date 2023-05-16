from random import randint

with open('numeros_randomicos.txt', 'w', encoding='utf-8') as file:
    for n in range(100):
        file.write(str(randint(1000, 10000)) + '\n')