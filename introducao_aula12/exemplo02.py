import csv

lista = [['abacate'], ['uva'], ['kiwi']]

with open('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/introducao_aula12/exemplo02.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(lista)