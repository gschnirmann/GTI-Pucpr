import datetime
from decimal import Decimal


ano_atual = datetime.datetime.today().year

print("Seja bem vindo à DARK SIDE STORE!")
print("Meu nome é Darth Sidious.")
print("Irei fazer a análise do seu limite, por favor:\n")

cargo_empresa = input("\nInforme o seu cargo atual?\n")

while True:
    try:
        salario = Decimal(input("\nInforme o seu último salário:\n"))
        if not salario > 0:
            raise ValueError("O salário informado é inválido.\nPor Favor:")
    except:
        print("\nO salário informado é inválido.\nPor Favor:")
    else:
        break

while True:
    try:
        ano_nascimento = int(input("\nInforme seu ano de nascimento?\n"))
        if not  ano_atual > ano_nascimento or ano_nascimento <= 1000:
            raise ValueError("O ano informado é inválido.\nPor Favor:")
    except ValueError as e:
        print("\nO ano informado é inválido.\nPor Favor:")
    else:
        break

idade_aproximada = ano_atual - ano_nascimento
limite = round(salario * Decimal(idade_aproximada / 1000) + 100 , 2)

print("\nConforme o informado:\n")
print("Você atualmente é:" , cargo_empresa.upper())
print("Seu último salário foi de R$:{:.2f}".format(salario))
print("Você nasceu em:" , ano_nascimento)
print("Sua idade aproximada é de:", idade_aproximada , "anos.")
print("Com base nas informações passadas seu limite é de R${:.2f}" .format(limite) , "\n")
while True:
    validacao = input("\nAs informações estão corretas (S/N)?\n")
    if validacao == "s" or validacao == "S":
        print("\nMaravilha!\nVamos continuar então\n")
        break
    elif validacao == "n" or validacao == "N":
        print("\nEscolha a informação que deseja alterar:\n")
        opcao = int(input("1 - Cargo\n2 - Salário\n3 - Ano de Nascimento\n"))
        if opcao == 1:
            cargo_empresa = input("\nInforme o seu cargo atual?\n")
        elif opcao == 2:
            while True:
                try:
                    salario = Decimal(input("\nInforme o seu último salário:\n"))
                    if not salario > 0:
                        raise ValueError("O salário informado é inválido.\nPor Favor:")
                except:
                    print("\nO salário informado é inválido.\nPor Favor:")
                else:
                    break
        elif opcao == 3:
            while True:
                try:
                    ano_nascimento = int(input("\nInforme seu ano de nascimento?\n"))
                    if not  ano_atual > ano_nascimento or ano_nascimento <= 1000:
                        raise ValueError("O ano informado é inválido.\nPor Favor:")
                except ValueError as e:
                    print("\nO ano informado é inválido.\nPor Favor:")
                else:
                    break
        idade_aproximada = ano_atual - ano_nascimento
        limite = round(salario * Decimal(idade_aproximada / 1000) + 100 , 2)
        print("\nConforme atualização de informações:\n")
        print("Você atualmente é:" , cargo_empresa)
        print("Seu último salário foi de R$:{:.2f}".format(salario))
        print("Você nasceu em:" , ano_nascimento)
        print("Sua idade aproximada é de:", idade_aproximada , "anos.")
        print("Com base nas informações passadas seu limite é de R${:.2f}" .format(limite) , "\n")
    else:
        print("\nA opção escolhida é inválida\nEscolha uma opção válida.")
