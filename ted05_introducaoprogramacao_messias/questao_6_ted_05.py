convidados = ['Kaká', 'Ronaldo', 'Ronaldinho', 'Adriano', 'Romário']

for convidado in convidados:
    print(f'\nOlá, {convidado}! Você foi convidado para a minha festa que acontecerá dia 31 de fevereiro de 2000!\n')

ausente = 'Adriano'
convidados.remove(ausente)
print(f'\nInfelizmente, {ausente} não poderá comparecer à festa.\n')

novo_convidado = 'Bebeto'
convidados.append(novo_convidado)
print(f'\nO convidado {ausente} será subsituído por {novo_convidado}.\n')

for convidado in convidados:
    print(f'\nOlá, {convidado}! Você foi convidado para a minha festa que acontecerá dia 31 de fevereiro de 2000!\n')