"""
Loop for para iterar um Nº de vezes
While itera até cumprir uma condição
"""

"""————— For ——————"""
for x in range(1,11):
    print(x)

# conteio regressivo com função reversed
for x in reversed(range(1,11)):
    print(x)
print("Feliz ano novo!!!")

# iterar sobre string
card_number = "1234-0000-0000-5678"
print("-"*10, " Aqui começa o Nº do cartão ", "-" * 10)
for x in card_number:
    print(x)
print("-"*10, " Aqui termina o Nº do cartão ", "-" * 10)

# argumento continue e break
for x in range(1, 21, 2):  # itera desde o 1 até 20 por cada 2 valores
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):  
    if x == 13:
        break  # sai do loop 'quebra o loop'
    else:
        print(x)

"""————— While —————"""
a = 8
while a > 0:
    a -= 1
    print(a)

games = ["COD", "GTA VI", "FIFA 2026"]
while games:    # durante exista um valor na lista
    print(games.pop(-1))    # imprime e retira último valor 

# argumento break
r = 15
while r >0:
    r -= 1
    if r == 7:
        print(f"Saida do loop por chegar até {r}")
        break
    print (r)

# argumento coninue
t = 15
while t >0:
    t -= 1
    if t == 7:
        print(f"Aqui o loop continua sem imprimir o {t}")
        continue
    print (t)

# condição else para correr código quando o while é False
languages = ["Python", "JavaScript", "XML", "HML"]
while languages:
    print(languages.pop(-1))
else:
    print("No more languages")