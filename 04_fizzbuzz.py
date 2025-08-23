def fizzbuzz():
    """
    Receve um número definido pelo utilizador e retorna
    'Fizz' ==> multiplo de 3
    'Buzz' ==> multiplo de 5
    'FizzBuzz ==> multiplo de ambos
    caso contrario devolve o mesmo input
    """
    try:
        num = int(input("Ingresse um número: "))
        
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
    except:
        print("Ocurrio um erro\nPor favor ingresse um número")

fizzbuzz()