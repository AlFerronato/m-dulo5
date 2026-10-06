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
def desfazer():
    if not undo:
        raise ValueError
    sku,amount =undo.pop()
    inventory[sku]["quantity"] += amount
fila =deque()
undo = []
fila.append(("A100",1))
fila.append(("B205",2))
fila.append(("A100",5))
sku,amount = fila.popleft() #o pedido e consumido antes, entao mesmo que a venda seja rejeitada, ele ja tira o pedido da fila
try:
    sell(inventory,sku,amount)
    undo.append((sku,amount))
except ValueError:
    pass

class robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print(f"Meu nome e: "+ self.name)
# r1 = robot()
# r1.name = "Tom"
# r1.color = "Azul"
# r1.weight = 30
# r1.introduce_self()
r1 = robot("Tom","Azul",30)
r2 = robot("joao","Vermelho",50)
# r1.introduce_self()
# r2.introduce_self()

class Person:
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p
        self.is_sitting=i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
p1 = Person("jose","bravo",False)
p2 = Person("Nicolas","Alegre",True)
p1.robot_owned = r2
p2.robot_owned = r1
p1.robot_owned.introduce_self()


# r2 = robot()
# r2.name= "joao"
# r2.color = "Vermelho"
# r2.weight = 50
# r2.introduce_self()