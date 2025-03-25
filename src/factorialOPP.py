"""
factorial_OOP.py
Calcula el factorial de un número o de un rango utilizando programación orientada a objetos.

Autor: Dr.P.E.Colla (c) 2022
Modificado por: [Tu Nombre]
Licencia: Creative Commons
"""

import sys

class Factorial:
    def __init__(self):
        """Inicializa la clase Factorial sin parámetros."""
        pass

    def calcular(self, n):
        """Calcula el factorial de un número entero no negativo."""
        if n < 0:
            print(f"Error: No se puede calcular el factorial de {n} porque es negativo.")
            return None
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    def run(self, min_val, max_val):
        """Calcula los factoriales en el rango [min_val, max_val]."""
        for num in range(min_val, max_val + 1):
            resultado = self.calcular(num)
            if resultado is not None:
                print(f"Factorial {num}! = {resultado}")

if __name__ == "__main__":
    # Verifica que se ingresó un argumento
    if len(sys.argv) < 2:
        print("Debe informar un número o un rango!")
        sys.exit(1)

    entrada = sys.argv[1]
    fact_obj = Factorial()

    try:
        # Caso: "-hasta" (ejemplo: "-10") → Rango [1, 10]
        if entrada.startswith("-"):
            fin = int(entrada[1:])
            if fin < 1:
                print("Error: El número debe ser mayor o igual a 1.")
                sys.exit(1)
            inicio = 1

        # Caso: "desde-" (ejemplo: "15-") → Rango [15, 60]
        elif entrada.endswith("-"):
            inicio = int(entrada[:-1])
            if inicio > 60:
                print("Error: El número debe ser menor o igual a 60.")
                sys.exit(1)
            fin = 60

        # Caso: "desde-hasta" (ejemplo: "4-8") → Rango [4, 8]
        elif "-" in entrada:
            inicio, fin = map(int, entrada.split("-"))
            if inicio > fin:
                print("Error: El inicio del rango no puede ser mayor que el final.")
                sys.exit(1)

        # Caso: Un solo número (ejemplo: "5") → Rango [5, 5]
        else:
            inicio = fin = int(entrada)

        print(f"Calculando factoriales desde {inicio} hasta {fin}:")
        fact_obj.run(inicio, fin)

    except ValueError:
        print("Error: Entrada inválida. Debe ingresar un número entero o un rango válido.")
        sys.exit(1)
