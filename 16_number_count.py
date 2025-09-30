

while True:
    list_number = [int(x) for x in input("Insert a list of numbers separeta by space please: ").split(" ")]
    if list_number:
        break

unique_numbers = set(list_number)
number_dict = {}

print(f'Original list: {list_number}')
print(f'Unique numbers: {unique_numbers}')

sort_list = sorted(list_number)

for value in sort_list:
    if number_dict.get(value):
        number_dict[value] += 1
    else:
        number_dict[value] = 1

for num, count in number_dict.items():
    print(f'{num}: {count}')