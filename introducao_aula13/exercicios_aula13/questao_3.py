def converte_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
print(converte_tempo(int(input('Insira um número inteiro para ser convertido em segundos: '))))