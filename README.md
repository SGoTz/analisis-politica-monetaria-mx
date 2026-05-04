# Transmisión de Política Monetaria en México: Tasa de Interés vs Inflación

## Descripción del Proyecto
Este proyecto analiza el mecanismo de transmisión de la política monetaria en México, evaluando cómo los cambios en la Tasa de Interés Interbancaria de Equilibrio (TIIE a 28 días) dictada por el Banco de México (Banxico) impactan en el Índice Nacional de Precios al Consumidor (INPC). 

El análisis se aborda desde una perspectiva metodológica dual:
1. **Econometría Estructural:** Uso de modelos de Vectores Autorregresivos (VAR) y Funciones de Impulso-Respuesta (IRF) para entender la causalidad y temporalidad del efecto de la tasa sobre los precios.
2. **Machine Learning:** Implementación de un modelo Gradient Boosting (XGBoost) para evaluar la capacidad predictiva no lineal de la inflación a corto plazo, utilizando rezagos (*lags*) de las variables macroeconómicas.

## Tecnologías y Librerías
* **Lenguaje:** Python 3.x
* **Extracción de Datos:** `requests`, `python-dotenv`
* **Manipulación y Procesamiento:** `polars` (para operaciones ultrarrápidas), `pandas`, `numpy`
* **Modelado Econométrico:** `statsmodels` (ADF Test, VAR, IRF)
* **Machine Learning:** `xgboost`, `scikit-learn`
* **Visualización:** `matplotlib`, `seaborn`

## 📂 Estructura del Repositorio
```text
📦 Prediccion-Inflacion-Mexico
 ┣ 📂 data
 ┃ ┣ 📂 raw                # Datos originales extraídos de la API (no subidos por tamaño/seguridad)
 ┃ ┗ 📂 processed          # Series de tiempo limpias, mensualizadas y estacionarias
 ┣ 📂 notebooks            # Jupyter Notebooks con el análisis exploratorio, VAR y ML
 ┣ 📂 src                  # Scripts de Python (ej. extracción automatizada de Banxico)
 ┣ 📜 .gitignore           # Archivos y carpetas excluidas del control de versiones
 ┣ 📜 README.md            # Documentación del proyecto
 ┗ 📜 requirements.txt     # Dependencias necesarias para ejecutar el proyecto