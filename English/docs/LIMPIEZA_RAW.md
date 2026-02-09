# Cleaning Rules (RAW -> INTERIM -> PROCESSED)

## 1. Input
- Official input: `data/raw/survey_covid_2021.xlsx`
- Working sheet: `BD`

## 2. Main transformations
1. Rename long original columns into technical field names.
2. Remove PII:
- `email`
- `name`
3. Text normalization:
- trim spaces
- collapse repeated spaces
- normalize known variants (`Si`, `Negativa.`, etc.)
4. Standardize Likert scale:
- `Nunca`
- `Casi nunca`
- `De vez en cuando`
- `Casi siempre`
- `Siempre`
5. Combined Likert responses:
- If multiple options are stored in one cell, keep the first valid option.
6. Timestamp:
- Convert Excel serial values to datetime when required.

## 3. Outputs
- `data/interim/survey_clean_stage.csv`
- `data/processed/survey_analytics.csv`
- `data/interim/survey_clean_stage.parquet` (if `pyarrow` available)
- `data/processed/survey_analytics.parquet` (if `pyarrow` available)

## 4. Derived variables
- Likert score per item:
- `q10_stress_score`
- `q11_optimism_score`
- `q12_control_score`
- `q13_protocols_score`
- `q14_anxiety_score`
- Final ordinal score:
- `q15_wellbeing_score`

## 5. Expected quality state
- No PII fields in `interim` and `processed`.
- Standardized category catalogs.
- Fully reproducible script-based workflow.
