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
Calcula el factorial de un número ingresado por el usuario.

Autor: Dr.P.E.Colla (c) 2022
Licencia: Creative Commons
"""

import sys

def factorial(n): 
    """Calcula el factorial de un número entero no negativo."""
    if n < 0: 
        print("Error: El factorial de un número negativo no existe.")
        return None
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

if __name__ == "__main__":
    # Verifica que se ingresó un argumento
    if len(sys.argv) < 2:
        print("Debe informar un número!")
        sys.exit(1)

    # Manejo de error al convertir argumento a entero
    try:
        numero = int(sys.argv[1])  # Se cambia 'num' por 'numero' para evitar redefiniciones
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        sys.exit(1)

    resultado = factorial(numero)

    if resultado is not None:
        print(f"Factorial {numero}! es {resultado}")
