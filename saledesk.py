from collections import deque


class Inventory:
    def __init__(self, starting_quantities):
        self._quantities = {}
        for sku, value in starting_quantities.items():
            quantity = value["quantity"] if isinstance(value, dict) else value
            self._quantities[sku] = quantity

    def quantity(self, sku):
        if sku not in self._quantities:
            raise ValueError("SKU desconhecido")
        return self._quantities[sku]

    def sell(self, sku, amount):
        quantity = self.quantity(sku)
        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if amount > quantity:
            raise ValueError("Quantidade insuficiente")
        self._quantities[sku] -= amount
        return self._quantities[sku]


class SaleDesk:
    def __init__(self, starting_quantities):
        self._inventory = Inventory(starting_quantities)
        self._pending = deque()
        self._history = []

    def quantity(self, sku):
        return self._inventory.quantity(sku)

    def submit(self, sku, amount):
        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")
        self._inventory.quantity(sku)
        self._pending.append((sku, amount))
        return len(self._pending)

    def process_next(self):
        if not self._pending:
            raise ValueError("Nao existem pedidos pendentes")
        sku, amount = self._pending.popleft()
        remaining = self._inventory.sell(sku, amount)
        self._history.append((sku, amount))
        return remaining