'''Criando um identificador de variável chamado nome atribuindo uma string ao identificador'''

name = input('Please, state your name:')
print(f'Hello,{name}')

age = int(input('State your age:'))
print(f'Age {age} | type {type(age)}')

age = input('State your age:')
print(f'Age {age} | type {type(age)}')

#Utilizando função sep= do print
print('day', 'month', 'year', sep='/')

print('b', 'n', 'n', '.', sep='a')

a = 3
b = 4
c = 5
sum = a + b + c
print(sum)