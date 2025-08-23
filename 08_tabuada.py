"""
Objetivo é criar uma função que retorna a tabuada do valor
inserido pelo utilizador
"""

def tabuada():
    
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

    for i in range(1,11):
        result = number * i
        print (f"{number} x {i} = {result}")


tabuada()