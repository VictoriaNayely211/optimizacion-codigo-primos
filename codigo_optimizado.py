import time
import math
import numpy as np

def es_primo_rapido(n: int) -> bool:
    """Verifica si un número es primo iterando solo hasta la raíz cuadrada."""
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

def main():
    inicio = time.time()

    # Usamos NumPy para crear el rango de números
    numeros = np.arange(1, 100_001, dtype=np.int64)

    # Usamos list comprehension para generar la lista de primos
    primos = [int(n) for n in numeros if es_primo_rapido(int(n))]

    fin = time.time()
    duracion = fin - inicio

    print(f"Se encontraron {len(primos)} números primos entre 1 y 100000.")
    print(f"Tiempo de ejecución (código optimizado): {duracion:.4f} segundos")

if __name__ == "__main__":
    main()
