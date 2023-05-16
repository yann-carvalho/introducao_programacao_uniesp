import csv

with open ('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/ted_11_12/filmes.csv', 'r', newline='', encoding='utf-8') as arquivo:
    arquivo_lido = csv.reader(arquivo)
    for linha in arquivo_lido:
            print(linha)