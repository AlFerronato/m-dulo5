price = [120,85,230]
def aplicar_desconto(price,desconto):
    for index in range(len(price)):
        price[index]= price[index] * (1 -desconto)

aplicar_desconto(price,0.1)
print(price)

def add_item(cart, item):
    cart.append(item)

def aumentar(number):
    number=number+1

cart = ["garrafa"]
count = 1
add_item(cart,"caneta")
aumentar(count)
print(cart)
print(count)
    