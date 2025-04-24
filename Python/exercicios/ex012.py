preco = float(input('Insira o preço do produto:R$ '))
precoTotal = preco - preco * 5 / 100
print('O preço do produto com desconto é R${}'.format(precoTotal))