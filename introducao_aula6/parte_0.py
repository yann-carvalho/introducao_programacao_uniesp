print('Digite uma opção do Menu')
print('1 - Empréstimo')
print('2 - Financiamento')
print('3 - Consórcio')

op_menu = int(input('Selecione uma opção: '))

if op_menu == 1:
    print('Você selecionou Empréstimo!')
elif op_menu == 2:
    print('Você selecionou Financiamento!')
elif op_menu == 3:
    print('Você selecionou Consórcio!')
else:
    print('Opção inválida!')
