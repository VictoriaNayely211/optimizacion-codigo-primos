import time
import subprocess
import statistics
import matplotlib.pyplot as plt

def medir(script, repeticiones=3):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.time()
        subprocess.run(["python", script], check=True)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

def main():
    tiempos_original = medir("codigo_original.py")
    tiempos_optimizado = medir("codigo_optimizado.py")

    print("Tiempos código original:", tiempos_original)
    print("Tiempos código optimizado:", tiempos_optimizado)

    # Distribución — Histograma
    plt.figure()
    plt.hist(tiempos_original, alpha=0.5, label="Original")
    plt.hist(tiempos_optimizado, alpha=0.5, label="Optimizado")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de tiempos")
    plt.legend()
    plt.savefig("distribucion_tiempos.png", dpi=150)

    # Comparación de medias
    prom_original = statistics.mean(tiempos_original)
    prom_optimizado = statistics.mean(tiempos_optimizado)

    plt.figure()
    plt.bar(["Original", "Optimizado"], [prom_original, prom_optimizado])
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos promedio")
    plt.savefig("comparacion_tiempos.png", dpi=150)

if __name__ == "__main__":
    main()
