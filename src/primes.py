# #!/usr/bin/python3
# # Python program to display all the prime numbers within an interval

# lower = 1
# upper = 500

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

def is_prime(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Optimización con raíz cuadrada
        if n % i == 0:
            return False
    return True

def primes_in_range(lower, upper):
    """Retorna una lista de números primos en un intervalo."""
    return [num for num in range(lower, upper + 1) if is_prime(num)]

if __name__ == "__main__":
    lower = 1
    upper = 500

    primes = primes_in_range(lower, upper)
    print(f"Números primos entre {lower} y {upper}:")
    print(", ".join(map(str, primes)))

    #Comentario para el tp1 modificacion
    