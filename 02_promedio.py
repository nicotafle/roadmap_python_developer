def media(*args):
    """
    Esta função calcula a media das notas e devolve
    se o aluno passou ou não
    + Para passar a média deve ser >= 7
    """
    total = 0
    
    for i in list(args):
        total += i

    media = total / len(list(args))

    if media >= 7:
        print(f"Parabens você passou o test com uma média de {media}")
    else:
        print(f"Lo lamento, mas você não passou o test, tirou uma média de {media}")


media(7.5, 8.3)