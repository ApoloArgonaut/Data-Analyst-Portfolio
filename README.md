# Data Analyst Portfolio (Bilingual Structure)

This repository is organized into two complete project spaces:

- `Español/` -> Full project in Spanish.
- `English/` -> Full project in English.

Each folder includes:
- Data pipeline (`raw -> interim -> processed`)
- Notebooks
- Statistical report
- Streamlit dashboard
- Portfolio landing files (`.md` and `.pdf`)

## Quick start

### Spanish version
```bash
cd Español
source ../.venv/bin/activate
python src/data/clean_survey.py
streamlit run app/streamlit_app.py
```

### English version
```bash
cd English
source ../.venv/bin/activate
python src/data/clean_survey.py
streamlit run app/streamlit_app.py
```

## Docker

### Build image
```bash
docker build -t data-analyst-portfolio .
```

### Run dashboard (English)
```bash
docker run --rm -p 8501:8501 -e PROJECT_DIR=English data-analyst-portfolio
```

### Run dashboard (Spanish)
```bash
docker run --rm -p 8502:8501 -e PROJECT_DIR=Español data-analyst-portfolio
```

### Docker Compose
```bash
docker compose up dashboard-en
docker compose up dashboard-es
```
