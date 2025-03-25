import os
import matplotlib.pyplot as plt


def collatz_steps(n):
    """Calcula la cantidad de pasos para llegar a 1 siguiendo la conjetura de Collatz"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1  # Conjetura 2n+1
        steps += 1
    return steps


# Generar datos para el gráfico
n_values = list(range(1, 10001))
iterations = [collatz_steps(n) for n in n_values]

output_dir = "src"

# Graficar los datos
plt.figure(figsize=(10, 6))
# Puntos dispersos para mejor visualización
plt.scatter(iterations, n_values, color="blue", s=1)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial")
plt.title("Número de Collatz y sus Iteraciones")
plt.grid(True)

# Guardar la imagen en la carpeta "src"
plt.savefig(os.path.join(output_dir, "collatz_plot.png"))
plt.show()
