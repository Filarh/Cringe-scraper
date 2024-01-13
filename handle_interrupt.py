from funciones.guardar_resultados import guardar_resultados
def handle_interrupt(signum, frame,jpath, resultados):
    print('InterrupciÃ³n detectada. Guardando resultados, y saliendo.')
    guardar_resultados(jpath, resultados)
    exit()