import json
def verificar(inventory,sku,amount):
    if sku not in inventory:
        print("SKU desconhecido")
        return False
    elif amount <= 0:
        print("Quantidade deveria ser positivo")
        return False
    return True

def gravar(transactions,actions,amount,sku):
    transactions.append({"actions":actions,"amount":amount,"sku":sku})        
def vender(inventory,transactions,amount,sku,changed_skus):
    if verificar(inventory,sku,amount) == True:
        if inventory[sku]["quantity"]< amount:
            print("estoque insuficiente")
            return
        else:
            inventory[sku]["quantity"] -= amount
            changed_skus.add(sku)
            gravar(transactions,"Venda",amount,sku)
def reabastecer(inventory,transactions,amount,sku,changed_skus):
    if verificar(inventory,sku,amount) == False:
        return
    inventory[sku]["quantity"] += amount
    changed_skus.add(sku)
    gravar(transactions,"Reabastecimento",amount,sku)
def total_estoque(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["quantity"] 
    return total
def low_stock_skus(inventory,threshold):
    resultado = []
    for sku, item in inventory.items():
        if item["quantity"]<=threshold:
            resultado.append(sku)
    return sorted(resultado)

def save_path(inventory,transactions,changed_skus,caminho):
    estado = {
        "inventory" : inventory,
        "transactions" : transactions,
        "changed_skus" : list(changed_skus)
    }
    with open(caminho,"w") as arquivo:
        json.dump(estado,arquivo)
def open_path(caminho):
    with open(caminho,"r") as arquivo:
        estado = json.load(arquivo)
    return estado["inventory"],estado["transactions"], set(estado["changed_skus"])
def main():
    transactions = []
    changed_skus = set()
    inventory = {
    "A100": {"name": "Notebook", "price": 8.50, "quantity": 4},
    "B205": {"name": "Pen", "price": 1.75, "quantity": 12},
    }
    while True:
        print("1. Vender item")
        print("2. Reabastecer item")
        print("3. Ver valor total do estoque")
        print("4, Ver SKU com baixo estoque")
        print("5. Salvar estado")
        print("6. Carregar estado")
        print("7. Sair")
        opcao = input("Escolha uma opção (1-7): ")
        if opcao == "1":
            sku = input("Digite o SKU do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            vender(inventory,transactions,quantidade,sku,changed_skus)
        elif opcao =="2":
            sku = input("Digite o SKU do produto: ")
            quantidade = int(input("digite a quantidade: "))
            reabastecer(inventory,transactions,quantidade,sku,changed_skus)
        elif opcao =="3":
            print(total_estoque(inventory))
        elif opcao == "4":
            threshold = int(input("Digite um valor de limite mínimo: "))
            print(low_stock_skus(inventory,threshold))
        elif opcao == "5":
            save_path(inventory,transactions,changed_skus,"estado.json")
        elif opcao =="6":
            inventory,transactions,changed_skus = open_path("estado.json")

        elif opcao =="7":
            break