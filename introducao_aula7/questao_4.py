# Fácil: Faça um programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.
nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
nota3 = float(input('Insira sua terceira nota: '))
nota4 = float(input('Insira sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f'Sua média foi {media:.2f} e você foi aprovado por média!')
else:
    print(f'Sua média foi {media:.2f} e você não foi aprovado por média.')