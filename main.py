# Importar las funciones desde el archivo functions.py
# Importar los módulos necesarios
import urllib.request
import json
from bs4 import BeautifulSoup
import concurrent.futures
import signal as sgnl
from tqdm import tqdm
# Importar las funciones
from funciones.handle_interrupt import handle_interrupt
from funciones.guardar_resultados import guardar_resultados
from funciones.check_url import check_url

# Información sobre el rango de escaneo
desde = 0
hasta = 200

# para almacenar los resultados exitosos
success_results = []

# Lista de direcciones web
urls = ["https://hopepaste.download/?v=" + str(i).zfill(4) for i in range(desde, hasta + 1)]

# Ruta del archivo JSON principal
json_path = "output.json"
# Establecer el manejador de señales para CtrlC
# Pasar el tercer argumento (json_path) a la función handle_interrupt
sgnl.signal(sgnl.SIGINT, lambda signum, frame: handle_interrupt(signum, frame, json_path,success_results))

# Usar executor.map para aplicar la nueva función a cada url
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Utilizar tqdm para crear una barra de progreso
    with tqdm(total=len(urls), desc="Verificando URLs") as pbar:
        for result in executor.map(check_url, urls):
            # Actualizar la barra de progreso
            pbar.update(1)
            # Guardar el resultado en la lista o en el diccionario
            success_results.append(result)

print(result)
# Guardar los resultados al finalizar
guardar_resultados(json_path, success_results)