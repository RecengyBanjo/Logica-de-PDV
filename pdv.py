historico = []

print("=== PDV com Descontos ===")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    # Entrada do valor (com validação)
    valor = float(input("Valor da compra (R$): "))
    while valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.")
        valor = float(input("Valor da compra (R$): "))

    # Encerra o loop quando o valor for 0
    if valor == 0:
        break

    # Entrada da idade (com validação)
    idade = int(input("Idade do cliente: "))
    while idade < 0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.")
        idade = int(input("Idade do cliente: "))

    valor_final = valor

    # Regra 1: desconto por idade (>= 65 anos -> 20%)
    if idade >= 65:
        valor_final = round(valor_final * 0.8, 2)

    # Regra 2: desconto por valor (> 100 já com desconto de idade -> 10% extra)
    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}\n")

    # Guarda a compra no histórico
    historico.append([valor, idade, valor_final])

# Resumo do dia
total_bruto = 0
total_final = 0

for compra in historico:
    total_bruto += compra[0]
    total_final += compra[2]

total_descontos = total_bruto - total_final

print("\n=== RESUMO DO DIA ===")
print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
