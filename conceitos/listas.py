### LISTAS ###
"""
Tipo de dados que permite armazenar uma lista de elementos
é mutável, permite qualquer tipo de valor, permite accesar via índice
lista = []
"""

lista = ['Velez', 'Racing', 'River', 'Seleccion Argentina']

print(lista[0])     # Retorna 'Velez'
print(lista[-1])    # Retorna Seleccion Argentina

lista.append('Porto')   # Adiciona na última posição
print(lista[-1])    # Retorna Porto

lista.pop()         # Elimina o elemento no indice, por defeito é o último
print(lista[-1])    # Retorna Seleccion Argentina

lista.remove('River')   #Elimina elemento 'River'

print(len(lista))   # Quantidade de elementos dentro da lista


