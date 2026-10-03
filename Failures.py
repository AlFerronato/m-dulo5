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
    restante = vender(inventory,4,"A100")
    assert restante == 0
    assert inventory == {"A100":{"quantity":0}}
def teste_vender_zero():
    inventory = {"A100": {"quantity":5}}
    try:
        vender(inventory,0,"A100")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    assert inventory =={"A100":{"quantity":5}}
def teste_vender_negativo():
    inventory = {"A100":{"quantity":4}}
    try:
        vender(inventory,-2,"A100")
    except ValueError:
        pass
    else:
        raise AssertionError("Esperava ValueError")
    assert inventory == {"A100":{"quantity":4}}
def teste_vender_SKUdesconhecido():
    inventory = {"A100" :{"quantity":4}}
    try:
        vender(inventory,3,"C200")
    except ValueError:
        pass
    else:
        raise AssertionError("Esperava ValueError de SKU desconhecido")
    assert inventory == {"A100":{"quantity":4}}
def teste_2_vendas():
    inventory = {"A100":{"quantity":5}}
    primeira = vender(inventory,2,"A100")
    segunda = vender(inventory,1,"A100")
    assert primeira == 3
    assert segunda == 2
    assert inventory == {"A100":{"quantity":2}}
