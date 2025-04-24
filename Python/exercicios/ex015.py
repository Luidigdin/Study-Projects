km = float(input('Qual a distância percorrida? KM '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = dias * 60 + km * 0.15
print('O preço a ser pago por {} dias de aluguel e {}KM percorridos é de R${:.2f}'.format(dias, km, valor))