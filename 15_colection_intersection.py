### Exercicio 1 ###

while True:
    try:
        list_a = [int(number) for number in input("Insert a list with numbers (separate by whitespace):").split()]
        list_b = [int(number) for number in input("Insert a list with numbers (separate by whitespace):").split()]
        break
    except:
        print("Please insert only number separate by withespace")

print(f'Original first list: {list_a}')
print(f'Original second list: {list_b}')

set_a = set(list_a)
set_b = set(list_b)

intersection_nums = set_a.intersection(set_b)
print(f'The number whitin both lists are those:\n{intersection_nums}')

diference_nums = set_a.symmetric_difference(set_b)
print(f'The number that appears just at once list:\n{diference_nums}')

### Exercicio 2 ###

catalog = {
    1: {"name": "T-shirt", "price": 19.9, "stock": 34},
    2: {"name": "Jeans", "price": 59.9, "stock": 12}
}

catalog.update({
    3: {"name": "Shoes", "price": 75.9, "stock": 6},
    4: {"name": "Hat", "price": 15.9, "stock": 21}
})

for product in catalog.values():
    print('+'*60)
    for value in product:
        print(f'{value}: {product[value]}')

catalog[2]['stock'] -= 1
print(f"Our product {catalog[2]['name']} update stock is: {catalog[2]['stock']} units")
