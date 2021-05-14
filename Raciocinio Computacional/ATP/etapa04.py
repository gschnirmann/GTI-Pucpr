#Atp - Etapa4:
qtd_produto = int(input("Quantos produtos você deseja comprar?\n"))
compras = []
compras_produtos =[]
compras_precos =[]
soma_dos_precos = 0
for c in range(qtd_produto):
    produto = input("Qual o produto que você que comprar?\n")
    compras_produtos.append (produto)
    preco = float(input("Qual o preço do produto?\n"))
    while preco <= 0:
        preco = float(input("O valor informado é inválido.\nPor favor informe um valor válido:\n"))
    compras_precos.append (preco)

    for preco in compras_precos:
        soma_dos_precos = sum(compras_precos)


print("Os produtos que você informou são:")

print(*(compras_produtos),"\n" , *(compras_precos) , "\n")
print("O total da sua compra é de R$: " , soma_dos_precos)
