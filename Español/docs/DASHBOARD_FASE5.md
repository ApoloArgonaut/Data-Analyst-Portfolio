# Fase 5 - Dashboard

## Objetivo
Presentar insights del analisis en una interfaz interactiva para exploracion rapida y comunicacion ejecutiva.

## App
- Ruta: `app/streamlit_app.py`
- Fuente de datos: `data/processed/survey_analytics.csv`

## Funcionalidades incluidas
- Filtros por genero, impacto percibido, bienestar final y rango de fecha.
- KPIs de seguimiento:
- `% impacto negativo`
- `% reporta problemas`
- `% bajo bienestar (No/Tal vez)`
- `% ansiedad alta`
- Visuales principales:
- Distribuciones de impacto y bienestar.
- Stack de bienestar por genero.
- Heatmap de problemas vs bienestar final.
- Promedios de scores emocionales.
- Tabla de pruebas chi-cuadrada (quick view).
- Export de datos filtrados.

## Ejecucion
```bash
source ../.venv/bin/activate
streamlit run app/streamlit_app.py
```

## Nota
La lectura de resultados debe considerar limitaciones de muestra no probabilistica y contexto 2021 (aprox. 5 anos de diferencia respecto al presente).  
Este dashboard reutiliza datos de un proyecto de clase para demostrar su transformacion a un caso practico profesional de Data Analyst.
