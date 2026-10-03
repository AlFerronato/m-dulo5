from debugger import sell
def test_successful_sale():
    inventory = {"A100": {"quantity": 4}}
    remaining = sell(inventory, "A100", 1)
    assert remaining == 3
    assert inventory == {"A100": {"quantity": 3}}

def test_overselling_preserves_state():
    inventory = {"A100": {"quantity": 4}}
    try:
        sell(inventory, "A100", 5)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    assert inventory == {"A100": {"quantity": 4}}

def vender(inventory,amount,sku,):
    if sku not in inventory:
        raise ValueError("SKU desconhecido")
    if amount <=0:
        raise ValueError("Quantidade deveria ser positivo")
    current = inventory[sku]["quantity"]
    if amount > current:
        raise ValueError("quantidade insuficiente")
    inventory[sku]["quantity"] -= amount
    return inventory[sku]["quantity"]

def teste_vender_todo_estoque():
    inventory = {"A100": {"quantity":4}}
    restante = sell(inventory,"A100",4)
    assert restante == 0
    assert inventory == {"A100":{"quantity":0}}
def teste_vender_zero():
    inventory = {"A100": {"quantity":5}}
    try:
        sell(inventory,"A100",0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    assert inventory =={"A100":{"quantity":5}}
def teste_vender_negativo():
    inventory = {"A100":{"quantity":4}}
    try:
        sell(inventory,"A100",-2)
    except ValueError:
        pass
    else:
        raise AssertionError("Esperava ValueError")
    assert inventory == {"A100":{"quantity":4}}
def teste_vender_SKUdesconhecido():
    inventory = {"A100" :{"quantity":4}}
    try:
        sell(inventory,"C200",3)
    except ValueError:
        pass
    else:
        raise AssertionError("Esperava ValueError de SKU desconhecido")
    assert inventory == {"A100":{"quantity":4}}
def teste_2_vendas():
    inventory = {"A100":{"quantity":5}}
    primeira = sell(inventory,"A100",2)
    segunda = sell(inventory,"A100",1)
    assert primeira == 3
    assert segunda == 2
    assert inventory == {"A100":{"quantity":2}}
print("TESTE 1")
test_successful_sale()

print("TESTE 2")
test_overselling_preserves_state()

print("TESTE 3")
teste_vender_todo_estoque()

print("TESTE 4")
teste_vender_zero()

print("TESTE 5")
teste_vender_negativo()

print("TESTE 6")
teste_vender_SKUdesconhecido()

print("TESTE 7")
teste_2_vendas()

print("TODOS PASSARAM")