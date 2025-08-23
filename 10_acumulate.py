""" 
Objetivo é obter a somatoria dos número multiplos de 3 e 5 
manores que N (definida pelo utilizador)
"""

def soma_multiplos():
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

    soma = 0
    for i in range(1, number):
        if i % 3 == 0:
            soma += i
        elif i % 5 == 0:
            soma += i
        else:
            continue
    
    print(f"Soma = {soma}")

soma_multiplos()