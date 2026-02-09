# Data Analyst Portfolio - COVID Survey Case

Proyecto de analisis en Python construido por fases, desde datos raw hasta dataset procesado para analisis y dashboard.

## Landing (entry point)
- Version Markdown: `PORTAFOLIO_LANDING.md`
- Version PDF: `PORTAFOLIO_LANDING.pdf`
- One-pager reclutamiento (MD): `PORTAFOLIO_ONE_PAGER.md`
- One-pager reclutamiento (PDF): `PORTAFOLIO_ONE_PAGER.pdf`

## Disclaimer
La informacion analizada en este proyecto fue recabada en **2021**, durante el auge de la pandemia por COVID-19, con una muestra pequena y no probabilistica.  
Se reutiliza una base de un proyecto academico para construir un caso practico serio de Data Analyst (pipeline, analisis estadistico y dashboard).

## Resumen Ejecutivo (visible rapido)
- Muestra analizada: **178** respuestas (2021).
- Impacto negativo percibido: **51.98%**.
- Reporte de problemas en pandemia: **67.23%**.
- Bienestar final en riesgo (`No/Tal vez`): **41.01%**.
- Asociaciones significativas:
- `q4_problems` vs `q15_wellbeing_final` (p=0.000033)
- `q4_problems` vs `anxiety_high` (p=0.034516)

Resumen completo en: `RESUMEN_EJECUTIVO.md`

## Estructura

```text
data/
  raw/
  interim/
  processed/
docs/
src/
notebooks/
reports/
```

## Inicio rapido

```bash
source ../.venv/bin/activate
pip install -r requirements.txt
python3 src/data/clean_survey.py
```

## Fase 4 (EDA e inferencia)

```bash
source ../.venv/bin/activate
jupyter notebook notebooks/00_resumen_ejecutivo.ipynb
jupyter notebook notebooks/01_eda.ipynb
```

El notebook `notebooks/01_eda.ipynb` incluye:
- KPIs base del caso.
- Cruces por genero y bienestar final.
- Pruebas de chi-cuadrada.
- Correlaciones de Spearman en variables ordinales.
- Modelo logistico exploratorio.

## Fase 5 (Dashboard)

```bash
source ../.venv/bin/activate
streamlit run app/streamlit_app.py
```

## Documentos clave
- `PORTAFOLIO_LANDING.md`
- `PORTAFOLIO_LANDING.pdf`
- `PORTAFOLIO_ONE_PAGER.md`
- `PORTAFOLIO_ONE_PAGER.pdf`
- `PARTE_TEORICA_PROYECTO.md`
- `PLAN_PROYECTO_ANALYST.md`
- `docs/LIMPIEZA_RAW.md`
- `docs/FASES_PROYECTO.md`
- `docs/DASHBOARD_FASE5.md`
- `reports/findings.md`
