idade_aproximada = ano_atual - ano_nascimento
limite = ((salario * (idade_aproximada / 1000)) + 100)
print("Sua idade aproximada é de:", idade_aproximada , "anos.")
print("Com base nessas informações seu limite é de R${:.2f}" .format (limite) , "\n")
