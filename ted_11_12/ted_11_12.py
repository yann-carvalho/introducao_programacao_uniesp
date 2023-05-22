import csv
from os import name, system

def limparLinha():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

            
def maiorPublicoDeFilmes(filmes):
    cabecalho = next(filmes)
    totalPublico = 0
    nomeDoFilme = ''
    anoDeExibicao = ''

    for i, filme in enumerate(filmes):
        coluna = float(filme[9])

        if coluna > totalPublico:
            totalPublico = coluna
            nomeDoFilme = filme[2]
            anoDeExibicao = filme[1]
        else:
            continue

    print('O filme com maior publico é -> ', nomeDoFilme)
    print('Total do publico -> ', totalPublico)
    print('Ano de exibição -> ', anoDeExibicao)

with  open('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/ted_11_12/filmes.csv', newline='', encoding='utf-8') as filmes:

    limparLinha()

    lerFilmes = csv.reader(filmes)

    maiorPublicoDeFilmes(lerFilmes)
