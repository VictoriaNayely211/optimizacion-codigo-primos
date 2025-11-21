import pstats

def generar_reporte(archivo_prof: str, archivo_salida: str, limite: int = 20):
    stats = pstats.Stats(archivo_prof)
    stats.sort_stats(pstats.SortKey.CUMULATIVE)
    with open(archivo_salida, "w") as f:
        stats.stream = f
        stats.print_stats(limite)

if __name__ == "__main__":
    generar_reporte("profiling_original.prof", "profiling_original.txt")
    generar_reporte("profiling_optimizado.prof", "profiling_optimizado.txt")
