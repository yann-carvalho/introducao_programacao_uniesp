nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média é {media} e você foi aprovado!")
else:
    print(f"Sua média é {media} e você foi reprovado!")