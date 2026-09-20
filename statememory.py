price = [120,85,230]
def aplicar_desconto(price,desconto):
    for index in range(len(price)):
        price[index]= price[index] * (1 -desconto)

aplicar_desconto(price,0.1)
print(price)
        