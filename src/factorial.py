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

    try:
        # Caso: "-hasta" (ejemplo: "-10")
        if entrada.startswith("-"):
            fin = int(entrada[1:])  # Extrae el número después del "-"
            if fin < 1:
                print("Error: El número debe ser mayor o igual a 1.")
                sys.exit(1)
            inicio = 1  # Empieza desde 1
            print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        
        # Caso: "desde-" (ejemplo: "15-")
        elif entrada.endswith("-"):
            inicio = int(entrada[:-1])  # Extrae el número antes del "-"
            if inicio > 60:
                print("Error: El número debe ser menor o igual a 60.")
                sys.exit(1)
            fin = 60  # Llega hasta 60
            print(f"Calculando factoriales desde {inicio} hasta {fin}:")

        # Caso: "desde-hasta" (ejemplo: "4-8")
        elif "-" in entrada:
            inicio, fin = map(int, entrada.split("-"))
            if inicio > fin:
                print("Error: El inicio del rango no puede ser mayor que el final.")
                sys.exit(1)

        # Caso: Un solo número (ejemplo: "5")
        else:
            inicio = fin = int(entrada)

        # Calcular factoriales en el rango determinado
        for num in range(inicio, fin + 1):
            resultado = factorial(num)
            if resultado is not None:
                print(f"Factorial {num}! = {resultado}")

    except ValueError:
        print("Error: Entrada inválida. Debe ingresar un número entero o un rango válido.")
        sys.exit(1)
