# #!/usr/bin/python
# #*-------------------------------------------------------------------------*
# #* factorial.py                                                            *
# #* calcula el factorial de un número                                       *
# #* Dr.P.E.Colla (c) 2022                                                   *
# #* Creative commons                                                        *
# #*-------------------------------------------------------------------------*
# import sys
# def factorial(num): 
#     if num < 0: 
#         print("Factorial de un número negativo no existe")
#         return 0
#     elif num == 0: 
#         return 1
        
#     else: 
#         fact = 1
#         while(num > 1): 
#             fact *= num 
#             num -= 1
#         return fact 

# if len(sys.argv) == 0:
#    print("Debe informar un número!")
#    sys.exit()
# num=int(sys.argv[1])
# print("Factorial ",num,"! es ", factorial(num)) 

#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative Commons                                                        *
#*-------------------------------------------------------------------------*

#!/usr/bin/python
"""
factorial.py
Calcula el factorial de un número o de un rango ingresado por el usuario.

Autor: Dr.P.E.Colla (c) 2022
Modificado por: [Tu Nombre]
Licencia: Creative Commons
"""

import sys

def factorial(n): 
    """Calcula el factorial de un número entero no negativo."""
    if n < 0: 
        print(f"Error: No se puede calcular el factorial de {n} porque es negativo.")
        return None
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

if __name__ == "__main__":
    # Verifica que se ingresó un argumento
    if len(sys.argv) < 2:
        print("Debe informar un número o un rango!")
        sys.exit(1)

    entrada = sys.argv[1]

    # Comprobar si es un rango (ejemplo: 4-8)
    if "-" in entrada:
        try:
            inicio, fin = map(int, entrada.split("-"))
            if inicio > fin:
                print("Error: El inicio del rango no puede ser mayor que el final.")
                sys.exit(1)

            for num in range(inicio, fin + 1):
                resultado = factorial(num)
                if resultado is not None:
                    print(f"Factorial {num}! = {resultado}")

        except ValueError:
            print("Error: Debe ingresar un rango válido en formato 'inicio-fin' (ejemplo: 4-8).")
            sys.exit(1)
    
    else:
        # Manejo de error al convertir argumento a entero
        try:
            numero = int(entrada)
            resultado = factorial(numero)
            if resultado is not None:
                print(f"Factorial {numero}! = {resultado}")

        except ValueError:
            print("Error: Debe ingresar un número entero válido o un rango 'inicio-fin'.")
            sys.exit(1)

