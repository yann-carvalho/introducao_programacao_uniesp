import csv

with open('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/introducao_aula12/exemplo01.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
        if int(row[1]) >= 30:
            print(f'{row[0]} tem mais de 30 anos!')