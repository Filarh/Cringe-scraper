def guardar_resultados():
    with open(json_path, 'w') as json_file:
        json.dump(success_results, json_file, ensure_ascii=False, indent=2)