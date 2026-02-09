# Resumen Ejecutivo del Proyecto

## Contexto
Este caso reutiliza una encuesta aplicada en **2021** durante el auge de la pandemia COVID-19.  
La muestra es **pequena y no probabilistica** (178 respuestas), por lo que los hallazgos se interpretan como asociaciones dentro de la muestra, no como causalidad ni generalizacion poblacional.

## Por que este proyecto existe
El objetivo fue transformar una base academica en un proyecto serio de Data Analyst, con:
- Pipeline reproducible (`raw -> interim -> processed`)
- Limpieza y trazabilidad de reglas
- Analisis descriptivo e inferencial
- Dashboard interactivo para comunicacion de resultados

## Hallazgos clave (muestra 2021)
- Respuestas analizadas: **178**
- Impacto negativo percibido: **51.98%**
- Personas que reportan problemas en pandemia: **67.23%**
- Bienestar final `No/Tal vez`: **41.01%**
- Asociaciones significativas:
- `q4_problems` vs `q15_wellbeing_final` (p=0.000033)
- `q4_problems` vs `anxiety_high` (p=0.034516)

## Valor para portafolio
Aunque la base es historica (2021), el valor profesional esta en la metodologia:
- Estandarizacion de datos reales con inconsistencias
- Evidencia estadistica con supuestos explicitados
- Producto final analitico (notebook + reporte + dashboard)

## Donde ver resultados rapidamente
- Notebook ejecutivo: `notebooks/00_resumen_ejecutivo.ipynb`
- Notebook completo: `notebooks/01_eda.ipynb`
- Reporte final: `reports/findings.md`
- Dashboard: `app/streamlit_app.py`
