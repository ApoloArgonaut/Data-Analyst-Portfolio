# Portfolio Landing - Data Analyst Case

## Pitch
Caso de Data Analyst construido sobre datos historicos reales (2021), transformando un proyecto academico en una entrega profesional con pipeline, analisis inferencial y dashboard.

## Contexto y aviso
- Fuente: Encuesta realizada en 2021 durante el auge de COVID-19.
- Muestra: 178 respuestas (pequena, no probabilistica).
- Uso actual: El caso se utilizara como portafolio para demostrar metodologia profesional y capacidad tecnica.
- Alcance inferencial: asociaciones dentro de la muestra, no causalidad ni extrapolacion poblacional fuerte.

## Que es lo que el proyecto demuestra/resuelve
- Estructura y limpia datos reales con ruido de captura.
- Estandariza catalogos, anonimiza PII y genera capas `raw -> interim -> processed`.
- Produce evidencia descriptiva + inferencial (chi-cuadrada, Spearman, modelo logistico exploratorio).
- Presenta resultados en notebook ejecutivo y dashboard interactivo.

## Resultados claves(executed)
- Respuestas analizadas: **178**
- Impacto negativo percibido: **51.98%**
- Reporte de problemas en pandemia: **67.23%**
- Bienestar final en riesgo (`No/Tal vez`): **41.01%**
- Asociaciones significativas:
- `q4_problems` vs `q15_wellbeing_final` (p=0.000033)
- `q4_problems` vs `anxiety_high` (p=0.034516)

## Fases del proyecto
- Fase 1: `data/raw/` (fuente inmutable).
- Fase 2: `src/data/clean_survey.py` -> `data/interim/`.
- Fase 3: dataset analitico en `data/processed/`.
- Fase 4: notebooks (`notebooks/00_resumen_ejecutivo.ipynb`, `notebooks/01_eda.ipynb`).
- Fase 5: dashboard Streamlit (`app/streamlit_app.py`).

## Como moverse dentro del repo
- Resumen ejecutivo: `RESUMEN_EJECUTIVO.md`
- Reporte de findings: `reports/findings.md`
- Notebook ejecutivo ejecutado: `notebooks/00_resumen_ejecutivo.executed.ipynb`
- Notebook EDA ejecutado: `notebooks/01_eda.executed.ipynb`
- Dashboard app: `app/streamlit_app.py`

## Correr de manera local
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/data/clean_survey.py
jupyter notebook notebooks/00_resumen_ejecutivo.ipynb
streamlit run app/streamlit_app.py
```

## Porque esto es importante
Este proyecto no solo muestra graficas: muestra criterio de datos, trazabilidad de limpieza, analisis defendible y comunicacion de resultados en formato ejecutivo, asi como lo que demostro de una manera pequeña como fue la crisis de la pandemia en el 2021.
