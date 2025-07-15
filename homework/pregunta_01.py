"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """


    # Leer el archivo línea por línea
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    lines = [line.rstrip() for line in lines if line.strip()]

    inicio_index = 0
    
    for i, line in enumerate(lines):
        if re.match(r"\s*\d+\s+",line):
            inicio_index = i
            break
    
    contenido = lines[inicio_index:]

    data = []
    fila_actual = None

    for line in contenido:
        if re.match(r"\s*\d+\s+", line):
            if fila_actual:
                data.append(fila_actual)

            parts = re.split(r"\s{2,}",line.strip(),maxsplit=3)
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(",", ".").replace("%", ""))
            palabras = parts[3].strip()
            fila_actual = [cluster, cantidad, porcentaje, palabras]
        
        else:
            if fila_actual:
                fila_actual[3] = fila_actual[3] + " " + line.strip()

    
    if fila_actual:
        data.append(fila_actual)

    
    for row in data:
        palabras = row[3]
        palabras = re.sub(r"\s+", " ", palabras)
        palabras = re.sub(r"\.$", "", palabras)
        palabras = re.sub(r"\s*,\s*", ", ", palabras)
        row[3] = palabras.strip()

    
    columns = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ]
    
    df = pd.DataFrame(data, columns=columns)
    return df
    
