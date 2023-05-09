with open('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/introducao_aula10/names.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

print(f'Linhas é do tipo {linhas}')
print('\n')

for linha in linhas:
    print(linha)