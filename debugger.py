def sell(inventory,sku,amount):
    if sku not in inventory:
        raise ValueError("SKU desconhecido")
    if amount <=0:
        raise ValueError("Quantidade deveria ser positivo")
    current = inventory[sku]["quantity"]
    if amount > current:
        raise ValueError("quantidade insuficiente")
    inventory[sku]["quantity"] -= amount
    return inventory[sku]["quantity"]

#def main():
    inventory = {"A100": {"quantity": 4}}
    print(sell(inventory, "A100", 5))
    print(inventory)

#if __name__ == "__main__":
    main()
#def test_successful_sale():
    inventory = {"A100": {"quantity": 4}}
    remaining = sell(inventory, "A100", 1)
    assert remaining == 3
    assert inventory == {"A100": {"quantity": 3}}

#def test_overselling_preserves_state():
    inventory = {"A100": {"quantity": 4}}
    try:
        sell(inventory, "A100", 5)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    assert inventory == {"A100": {"quantity": 4}}
