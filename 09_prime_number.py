"""
O objetivo é criar uma função que obtendo um número brindado
pelo utilizador, devolver se for 'número primo' ou 'não número primo
"""

def e_primo():

    while True:
        try:
            number = int(input("Ingresse um número positivo: "))
            if number > 0:
                break
            else:
                print("Entrada errada!!\nPor favor ingresse um número")
                pass
        except:
            print("Entrada errada!!\nPor favor ingresse um número")

    for i in range (2 , number+1):
        if number % i == 0 and number != i:
            print("Não é número primo")
            break
        elif number % i == 0 and number == i:
            print("É número primo")
        else:
            continue

e_primo()