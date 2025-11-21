import time

def es_primo_lento(n: int) -> bool:
    """Verifica si un número es primo con un método poco eficiente."""
    if n < 2:
        return False
    # Recorre todos los números desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    inicio = time.time()

    primos = []
    for numero in range(1, 100_001):  # 1 a 100000
        if es_primo_lento(numero):
            primos.append(numero)

    fin = time.time()
    duracion = fin - inicio

    print(f"Se encontraron {len(primos)} números primos entre 1 y 100000.")
    print(f"Tiempo de ejecución (código original): {duracion:.4f} segundos")

if __name__ == "__main__":
    main()
