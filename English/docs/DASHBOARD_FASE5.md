# Phase 5 - Dashboard

## Objective
Present analytical insights in an interactive interface for quick exploration and executive communication.

## App
- Path: `app/streamlit_app.py`
- Data source: `data/processed/survey_analytics.csv`

## Included functionality
- Filters by gender, perceived impact, final wellbeing, and date range.
- KPI layer:
- `% perceived negative impact`
- `% reporting problems`
- `% at-risk final wellbeing (No/Tal vez)`
- `% high anxiety`
- Main visuals:
- Impact and wellbeing distributions.
- Stacked final wellbeing by gender.
- Heatmap: problems vs final wellbeing.
- Mean emotional score bars.
- Quick Chi-square results table.
- Filtered CSV export.

## Run
```bash
source ../.venv/bin/activate
streamlit run app/streamlit_app.py
```

## Note
Results must be interpreted with the limits of a non-probabilistic 2021 sample (roughly five years before current context).  
The dashboard reuses class-project data to demonstrate a professional Data Analyst delivery.
