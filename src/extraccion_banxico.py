import requests
import polars as pl
import os
from dotenv import load_dotenv

# 1. Configuración de la API
#TOKEN = ''
load_dotenv()
TOKEN = os.getenv("BANXICO_TOKEN")

# Identificadores de las series de tiempo en Banxico:
# SF43783: TIIE a 28 días (Tasa de Interés)
# SF43718: Tipo de Cambio FIX (Pesos por Dólar)
# SP74665: INPC General (Base 2a quincena jul 2018=100)
SERIES = "SF43783,SF43718,SP74665"

# Rango de fechas (ej. desde el año 2010 hasta hoy)
FECHA_INICIO = "2010-01-01"
FECHA_FIN = "2026-05-01"

url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{SERIES}/datos/{FECHA_INICIO}/{FECHA_FIN}"

headers = {
    'Bmx-Token': TOKEN
}

def extraer_datos():
    print("Conectando a la API de Banxico...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("¡Conexión exitosa! Procesando datos...")
        data_json = response.json()
        
        # Lista para guardar los datos antes de convertirlos a DataFrame
        datos_procesados = []
        
        # Iteramos sobre cada serie económica devuelta
        for serie in data_json['bmx']['series']:
            id_serie = serie['idSerie']
            
            # Verificamos que la serie tenga datos
            if 'datos' in serie:
                for dato in serie['datos']:
                    datos_procesados.append({
                        'Fecha': dato['fecha'],
                        'Valor': float(dato['dato'].replace(',', '')),
                        'Serie': id_serie
                    })
        
        # 2. Transformación con Polars
        # Convertimos la lista de diccionarios en un DataFrame ultrarrápido
        df = pl.DataFrame(datos_procesados)
        
        # Convertimos la columna 'Fecha' a formato de fecha real
        df = df.with_columns(
            pl.col('Fecha').str.strptime(pl.Date, "%d/%m/%Y")
        )
        
# Pivoteamos la tabla (Sintaxis actualizada para Polars >= 1.0.0)
        df_pivot = df.pivot(
            values='Valor', 
            index='Fecha', 
            on='Serie'  # <-- Cambiamos 'columns' por 'on'
        ).rename({
            "SF43783": "TIIE_28",
            "SF43718": "Tipo_Cambio_FIX",
            "SP74665": "INPC"
        }).sort("Fecha")
        
        # 3. Guardado (Ruta corregida)
        # La ruta asume que ejecutas el script desde la raíz del proyecto
        ruta_guardado = "data/raw/datos_macro_mexico.csv"
        
        # Escribimos el archivo
        df_pivot.write_csv(ruta_guardado)
        print(f"Datos guardados exitosamente en: {ruta_guardado}")
        
        # Mostramos las primeras filas en la terminal
        print("\nPrimeras filas del dataset:")
        print(df_pivot.head())
        
    else:
        print(f"Error al conectar: Código {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    extraer_datos()