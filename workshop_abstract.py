from collections import deque
#from debugger import sell

inventory = {
    "A100":4,
    "B200":12
}
class SaleDesk:
    def __init__(self, starting_quantities):
        self._inventory = starting_quantities.copy()
        self._pending = deque()
        self._history = []
    #def starting(self):
    def quantity(self,sku):
        if sku not in self._inventory:
            raise ValueError
        return self._inventory[sku]

desk1 = SaleDesk(inventory)
desk2 = SaleDesk(inventory)
desk1._inventory["A100"] = 0
print(desk1.quantity("A100"))
print(desk2.quantity("A100"))