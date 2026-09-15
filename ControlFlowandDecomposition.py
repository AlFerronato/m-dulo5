temperatura = 31
if temperatura >= 30:
    print(" o dia esta quente")
for hour in range(3):
    print("calculando temperatura")


sales = [120,85,230]
for sale in sales:
    tax = sale *0.1
    print(sale +tax)

def total_taxa(tax_rate,sale):
    taxa = sale *tax_rate
    return sale + taxa

sales = [120,85,230]
for sale in sales:
    total = total_taxa(0.1, sale)
    print(total)

def diferenca(first,second):
    result = first - second
    return result

answer = diferenca(10,4)
print(answer)

def calculate_total(price,discount_rate,tax_rate):
    discount_price = price * (1-discount_rate)
    return discount_price * (1+tax_rate)

def show_totals(prices,discount_rate,tax_rate):
    for price in prices:
        total = calculate_total(price,discount_rate,tax_rate)
        print(f"Final total: {total:.2f}")

def main():
    prices= [120,85,230]
    show_totals(prices,0.1,0.12)
main()


print("novo")
def calcular_total(price,discount_rate,tax_rate):
    discounted_price = price* (1-discount_rate)
    total = discounted_price *(1+tax_rate)
    return total
def show_totals(prices,discount_rate,tax_rate):
    for price in prices:
        total = calcular_total(price,discount_rate,tax_rate)
        print(f"O total é {total:.2f}")

def main():
    prices = [120,85,230]
    show_totals(prices,0.1,0.12)
main()