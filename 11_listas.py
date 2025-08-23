
def create_list():
    """
    Criar uma lista de 5 elemetos recebidos do utilizador
    """
    lista = []
    for i in range(5):
        while True:
            try:
                number = int(input("Ingresse um número: "))
                break
            except ValueError:
                print("Entrada errada!!\nPor favor ingresse um número")
        lista.append(number)
    
    print(f"Lista criada: {lista}")
    print(f"Maior número da lista: {max(lista)}")
    print(f"Menor número da lista: {min(lista)}")
    print(f"Somatória da lista: {sum(lista)}")


def no_dupli_list():
    """
    Esta função recebe entradas para criar uma lista e imprime a lista original  
    e uma nova lista mantendo ordem mas sem duplicados
    """
    list_raw = []
    while True:
            while True:
                try:
                    number = int(input("--Para sair ingresse '0'--\nIngresse um número: "))
                    break
                except ValueError:
                    print("Entrada errada!!\nPor favor ingresse um número")
            if number == 0:
                break
            else:
                list_raw.append(number)
    
    res_list = []
    for element in list_raw:
        if element not in res_list:
            res_list.append(element)
        
    print(f"Lista original = {list_raw}\nLista sem duplicados = {res_list}")

no_dupli_list()