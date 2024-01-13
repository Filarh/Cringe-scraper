def handle_interrupt(signum, frame):
    print('InterrupciÃ³n detectada. Guardando resultados, y saliendo.')
    guardar_resultados()
    exit()