from collections import deque
from debugger import sell
history =[]
history.append(("A100",1))
history.append(("B200",2))
mais_recente=history.pop()
print(mais_recente)

pendente = deque()
pendente.append(("C300",1))
pendente.append(("D400",2))
pedido_antigo = pendente.popleft()
print(pedido_antigo)

inventory = {
    "A100":{"quantity":4},
    "B205":{"quantity":12}
}
fila =deque()
fila.append(("A100",1))
fila.append(("B205",2))
fila.append(("A100",5))
sku,amount = fila.popleft()
sell(inventory,sku,amount)
