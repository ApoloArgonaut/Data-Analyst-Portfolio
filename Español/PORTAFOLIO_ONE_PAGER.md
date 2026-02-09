# One-Pager · Data Analyst Portfolio (COVID 2021 Case)

## Elevator pitch
Transforme un proyecto academico de 2021 en una entrega profesional de Data Analyst con pipeline reproducible, analisis estadistico y dashboard ejecutivo.

## Contexto (importante)
- Datos recabados en 2021 durante el auge de la pandemia COVID-19.
- Muestra: 178 respuestas (no probabilistica, tamano pequeno).
- Uso actual: caso realista de portafolio para demostrar metodologia y ejecucion.

## Para reclutadores generales (no tecnico)
### Que problema resuelve
Convierte datos de encuesta con ruido en insights claros sobre bienestar emocional y factores asociados.

### Resultado de negocio
- 67.23% reporto problemas durante pandemia.
- 41.01% quedo en bienestar final de riesgo (`No/Tal vez`).
- Hallazgo central: reportar problemas se asocia significativamente con bienestar final y ansiedad.

### Lo que demuestra del candidato
- Pensamiento estructurado.
- Capacidad de convertir datos crudos en decisiones.
- Comunicacion ejecutiva y visual.

## Para reclutadores tecnicos (data/programacion)
### Stack
Python, pandas, scipy, scikit-learn, Jupyter, Streamlit.

### Rigor analitico
- Pipeline: `raw -> interim -> processed`.
- Limpieza trazable (normalizacion, manejo de inconsistencias, remocion de PII).
- Evidencia inferencial:
- `q4_problems vs q15_wellbeing_final` (Chi2, p=0.000033)
- `q4_problems vs anxiety_high` (Chi2, p=0.034516)
- Modelo logistico exploratorio: accuracy 0.733.

### Entregables
- Notebook ejecutivo: `notebooks/00_resumen_ejecutivo.executed.ipynb`
- Notebook EDA: `notebooks/01_eda.executed.ipynb`
- Reporte: `reports/findings.md`
- Dashboard: `app/streamlit_app.py`

## Disclaimer metodologico
Este caso no pretende inferencia causal ni generalizacion poblacional fuerte.  
El valor esta en la metodologia profesional aplicada sobre datos reales historicos.

## Enlaces clave
- Landing completa: `PORTAFOLIO_LANDING.md`
- PDF landing: `PORTAFOLIO_LANDING.pdf`
- Resumen ejecutivo: `RESUMEN_EJECUTIVO.md`
