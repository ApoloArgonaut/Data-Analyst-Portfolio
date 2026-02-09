# One-Pager · Data Analyst Portfolio (COVID 2021 Case)

## Elevator pitch
I transformed a 2021 academic project into a professional Data Analyst delivery with a reproducible pipeline, statistical analysis, and an executive dashboard.

## Context (important)
- Data collected in 2021 during the COVID-19 peak period.
- Sample: 178 responses (non-probabilistic, small size).
- Current use: realistic portfolio case to demonstrate methodology and execution.

## For general recruiters (non-technical)
### What problem this solves
Turns noisy survey data into clear insights about emotional wellbeing and associated factors.

### Business-facing outcome
- 67.23% reported problems during the pandemic.
- 41.01% ended in at-risk final wellbeing (`No/Tal vez`).
- Core finding: reporting problems is significantly associated with final wellbeing and anxiety.

### What this demonstrates
- Structured analytical thinking.
- Ability to turn raw data into decisions.
- Executive and visual communication.

## For technical recruiters (data/programming)
### Stack
Python, pandas, scipy, scikit-learn, Jupyter, Streamlit.

### Analytical rigor
- Pipeline: `raw -> interim -> processed`.
- Traceable cleaning (normalization, inconsistency handling, PII removal).
- Inferential evidence:
- `q4_problems vs q15_wellbeing_final` (Chi2, p=0.000033)
- `q4_problems vs anxiety_high` (Chi2, p=0.034516)
- Exploratory logistic model: accuracy 0.733.

### Deliverables
- Notebook ejecutivo: `notebooks/00_resumen_ejecutivo.executed.ipynb`
- Notebook EDA: `notebooks/01_eda.executed.ipynb`
- Reporte: `reports/findings.md`
- Dashboard: `app/streamlit_app.py`

## Methodological disclaimer
This case does not claim causal inference or strong population generalization.  
Its value is the professional methodology applied to historical real-world data.

## Enlaces clave
- Landing completa: `PORTAFOLIO_LANDING.md`
- PDF landing: `PORTAFOLIO_LANDING.pdf`
- Executive summary: `RESUMEN_EJECUTIVO.md`
