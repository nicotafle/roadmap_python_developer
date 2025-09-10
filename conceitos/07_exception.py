"""
É a forma de suportar erros sem quebrar o código
Existem muitos tipos de erros, alguns deles:
ZeroDivisionError, TypeError, ValueError
1. try | 2. except | 3. finally
"""

# print(10/0) Descomenta para ZeroDivisionError
try:
    print(10/0)
except ZeroDivisionError:
    print("Não é possível divir por 0")

# # print(4 + "Hello Word") Descomenta para TypeError
try:
    print(4 + "Hello Word")
except TypeError:
    print("É impossível sumar o int '4' com a str 'Hello Word'")

# # int("pizza") Descomenta para ValueError
try:
    int("pizza")
except:
    print("ValueError quando quer operar um metodo com argumentos do type errado")

def division():
    while True:
        try:
            x = int(input("Ingresse um número: "))
            print(1/x)
            break
        except ZeroDivisionError:
            print("Não pode dividir por 0!!!")
        except ValueError:
            print("Ingresse um NÚMERO por favor.")
        except Exception as e:
            print(f"Ocorreu o seguinte Error: {e}")
        finally:        # sempre é ativado existir erro ou não e sem importar o break ou não
            print("Aqui o bloque é finalizado")

division()

"""
————— É possivel criar uma exception —————
quando é precisso "romper" o código por não aceitar valores ou tipos
é possível definir um raise
"""

number = int(input("Numero: "))
if number > 10:
    raise Exception(f"O numero não pode exceder o valor 10. ({number})")
print(number)

