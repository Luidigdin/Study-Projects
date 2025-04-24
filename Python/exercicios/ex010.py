real = float(input('Digíte o valor em reais que você possui:R$ '))
dollar = real / 5.68
print('com R${} você pode comprar ${:.2f} hoje'.format(real, dollar))