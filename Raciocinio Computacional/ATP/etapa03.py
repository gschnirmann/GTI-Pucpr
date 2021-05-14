produto = input("Informe o produto que deseja comprar: \n")
precoProduto = float(input("Informe o preço do produto que deseja comprar: \n"))
nomeCompleto = "Paulo Henrique Rodrigues Pradella"
primeiroNome = "Paulo"
desconto = precoProduto - (precoProduto * (int(len(primeiroNome)) / 100))
if (precoProduto <= valorCredito * 0,60):
    print("Liberado!")
elif (precoProduto > (valorCredito * 0,60) and precoProduto >= (valorCredito * 0,90)):
    print("Liberado ao parcelar em até 2 vezes")
elif (precoProduto > (valorCredito * 0,90) and precoProduto >= (valorCredito * 1)):
    print("Liberado ao parcelar em até 3 vezes")
else:
    print("Bloqueado")

if (precoProduto >= int(len(nomeCompleto)) and precoProduto <= idadeAproximada):
    print("PARABÉNS! Você receberá um desconto de " , len(primeiroNome) , "%." ,
    "\nO novo valor do seu produto é de R$" , desconto)
