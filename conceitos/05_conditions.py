"""
Condicionais
if | elif | else
"""

# Estrutura

x = 100
y = 28

if x > y :
    print(f"{x} é maior que {y}")
elif x < y :
    print(f"{x} é menor que {y}")
else:
    print(f"{x} são iguais {y}")

# Definir numa linha

result = f"{x} é maior ou igual que {y}" if x>=y else f"{x} é menor que {y}"
print(result)

# Switch Statment - função que aciona (switch) utilizando dicionario e .get()
def switcher(value):
    switch ={
        "0": "Bom dia!",
        "1": "Boa tarde!",
        "2": "Boa noite!"
    }
    return switch.get(value, "Boa semana!")

print(switcher("3"))