n_conta = "1234-5"
saldo = 1000
debito = 1500
credito = 150

saldo_atual = (saldo - debito) + credito

if saldo_atual > 0:
    print(f"O saldo da conta {n_conta} é positivo")
else:
    print(f"O saldo da conta {n_conta} é negativo")