import json

lista = {
    'frutas': {'abacate': 6.99,
               'uva': 7.99,
               'kiwi': 13.99},
    'data': '2023-05-20'
}

with open('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/introducao_aula12/arquivo.json', 'w') as file:
    dados = json.load(file)
    json.dump(lista, file)
    my_json = json.dumps(lista)

valor_uva = dados['frutas']['uva']
print(valor_uva)