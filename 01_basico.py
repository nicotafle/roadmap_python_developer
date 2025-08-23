"""
Esta função vai solicitar nome, idade e altura ao utilizador
e vai calcular em base na idade o ano de nascimento, considere
o ano atual como 2025

return: mensagem formatada com a informação
"""

nome = str(input("Ingresse o seu nome: "))
idade = int(input("Ingresse a sua idade: "))
altura = float(input("Ingresse a sua altura (cm): "))

ano_nasci = 2025 - idade

print(f"{nome} nasceu no ano {ano_nasci}, e mede {altura} cm ")

