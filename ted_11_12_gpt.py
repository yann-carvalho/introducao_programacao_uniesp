import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/home/yannsoares/UNIESP/P1/introducao_programacao_uniesp/ted_11_12/filmes.csv')

# Encontrar o maior número na coluna específica
maior_numero = df['Público no ano de exibição'].max()

print(f'O maior número na coluna é: {maior_numero}')