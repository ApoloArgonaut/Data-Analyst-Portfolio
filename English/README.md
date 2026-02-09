# Data Analyst Portfolio - COVID Survey Case (English)

Phase-based Python analytics project, from raw data to a processed dataset, statistical analysis, and dashboard.

## Landing (entry point)
- Markdown version: `PORTAFOLIO_LANDING.md`
- PDF version: `PORTAFOLIO_LANDING.pdf`
- Recruitment one-pager (MD): `PORTAFOLIO_ONE_PAGER.md`
- Recruitment one-pager (PDF): `PORTAFOLIO_ONE_PAGER.pdf`

## Disclaimer
This dataset was collected in **2021**, during the peak period of the COVID-19 pandemic, using a small non-probabilistic sample.  
The current project reuses that class dataset as a serious portfolio case to demonstrate a professional Data Analyst workflow.

## Fast executive snapshot
- Sample analyzed: **178** responses (2021).
- Perceived negative impact: **51.98%**.
- People reporting pandemic-related problems: **67.23%**.
- At-risk final wellbeing (`No/Tal vez`): **41.01%**.
- Significant associations:
- `q4_problems` vs `q15_wellbeing_final` (p=0.000033)
- `q4_problems` vs `anxiety_high` (p=0.034516)

Full summary: `RESUMEN_EJECUTIVO.md` (English content, legacy file name kept for compatibility).

## Structure

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

## Quick start

```bash
source ../.venv/bin/activate
pip install -r requirements.txt
python src/data/clean_survey.py
```

## Phase 4 (EDA and inference)

```bash
source ../.venv/bin/activate
jupyter notebook notebooks/00_resumen_ejecutivo.ipynb
jupyter notebook notebooks/01_eda.ipynb
```

`notebooks/01_eda.ipynb` includes:
- Core KPIs
- Key cross-tab analysis
- Chi-square tests
- Spearman correlations for ordinal variables
- Exploratory logistic model

## Phase 5 (Dashboard)

```bash
source ../.venv/bin/activate
streamlit run app/streamlit_app.py
```

## Key documents
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
