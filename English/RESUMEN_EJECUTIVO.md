# Executive Summary

## Context
This case reuses a survey collected in **2021** during the peak COVID-19 period.  
The sample is **small and non-probabilistic** (178 responses), so findings should be interpreted as associations within this sample, not causal claims or broad population estimates.

## Why this project exists
The objective was to transform an academic dataset into a professional Data Analyst project with:
- Reproducible pipeline (`raw -> interim -> processed`)
- Documented cleaning and traceability
- Descriptive + inferential analysis
- Interactive dashboard for executive communication

## Key findings (2021 sample)
- Responses analyzed: **178**
- Perceived negative impact: **51.98%**
- Respondents reporting pandemic-related problems: **67.23%**
- Final wellbeing at risk (`No/Tal vez`): **41.01%**
- Significant associations:
- `q4_problems` vs `q15_wellbeing_final` (p=0.000033)
- `q4_problems` vs `anxiety_high` (p=0.034516)

## Portfolio value
Even with historical data (2021), the professional value is the methodology:
- Real-world data standardization with inconsistencies
- Statistical evidence with explicit assumptions
- End-to-end analytical product (notebooks + report + dashboard)

## Where to review quickly
- Executive notebook: `notebooks/00_resumen_ejecutivo.ipynb`
- Full EDA notebook: `notebooks/01_eda.ipynb`
- Findings report: `reports/findings.md`
- Dashboard: `app/streamlit_app.py`
