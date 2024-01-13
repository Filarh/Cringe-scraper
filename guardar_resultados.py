import json
def guardar_resultados(jpath, resultados):
    with open(jpath, 'w') as json_file:
        json.dump(resultados, json_file, ensure_ascii=False, indent=2)