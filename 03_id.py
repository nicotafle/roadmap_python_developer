"""Crie um programa que:

Solicite a idade de uma pessoa.
Pergunte se ela tem RG (sim ou não).
Se tiver 18 anos ou mais e tiver RG, exiba: "Entrada autorizada".
Caso contrário, exiba: 'Entrada negada'.
"""

def e_maior():
    """
    Esta função vai analisar os inputs *idade e *rg e vai devolver 
    se pode ingressar ou não
    """
    try:
        idade = int(input("Ingresse a sua idade em números: "))
        rg = bool(int(input("Tem RG?\nSim : 1 - Não : 0\n")))
        print(rg)
        print(bool(0))

        if idade >= 18 and rg == True:
            print("Entrada autorizada")
        else:
            print("Entrada negada")
    
    except Exception as e:
        print(f"Erro: {e}")
    
e_maior()