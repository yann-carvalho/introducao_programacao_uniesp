nome = input('Digite seu nome: ')
signo = input('Qual o seu signo? ')

pessoa = {
    'primeiro_nome': nome,
    'segundo_nome': 'Carvalho',
    'idade': 27,
    'cidade': 'João Pessoa',
    'signo': signo
}
print(f'Primeiro nome: {pessoa["primeiro_nome"]}')
print(f'Segundo nome: {pessoa["segundo_nome"]}')
print(f'Idade: {pessoa["idade"]}')
print(f'Cidade: {pessoa["cidade"]}')
print(f'Signo: {pessoa["signo"]}')