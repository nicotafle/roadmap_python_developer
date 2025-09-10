### LISTS ###

my_list = [1,55,309,2,45]

print(max(my_list)) # print maximun number
print(min(my_list)) # print minimun number

print(f"Lista ordem original: {my_list}")
my_list.reverse()
print(f"Lista ordem revertida: {my_list}")

### TUPLES ###

my_tuple = ('brown', 'red', 'green')

# my_tuple[0] = 'white'   Uncomment to TypeError 
print(my_tuple[0])

### SETS ###
while True:
    my_set = {word for word in input("Insert 5 words: ").lower().split(' ')}
    if len(my_set) == 5:
        break
    else:
        print("The user have to write just 5 words!")

print("List of unique words choiced by the user")
for word in my_set:
    print("* ", word)

### DICT ###

product = {
    "name" : "Computer",
    "price" : "€ 635",
    "Stock" : 123
}

product["category"] = "Gamer"

for k in product.keys():
    print(f"{k}: {product[k]}")