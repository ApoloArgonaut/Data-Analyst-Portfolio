# Reglas de Limpieza (RAW -> INTERIM -> PROCESSED)

## 1. Entrada
- Input oficial: `data/raw/survey_covid_2021.xlsx`
- Hoja de trabajo: `BD`

## 2. Transformaciones principales
1. Renombrado de columnas largas a nombres tecnicos cortos.
2. Eliminacion de PII:
- `email`
- `name`
3. Normalizacion textual:
- trim de espacios
- compactacion de espacios multiples
- correccion de variantes puntuales (`Si` -> `Si`, `Negativa.` -> `Negativa`)
4. Estandarizacion de escala Likert:
- `Nunca`
- `Casi nunca`
- `De vez en cuando`
- `Casi siempre`
- `Siempre`
5. Manejo de respuestas compuestas Likert:
- Si hay mas de una opcion en la celda, se conserva la primera opcion valida.
6. Timestamp:
- conversion de serial Excel a datetime.

## 3. Salidas
- `data/interim/survey_clean_stage.csv`
- `data/processed/survey_analytics.csv`
- `data/interim/survey_clean_stage.parquet` (si existe `pyarrow`)
- `data/processed/survey_analytics.parquet` (si existe `pyarrow`)

## 4. Variables derivadas
- Score Likert por item:
- `q10_stress_score`
- `q11_optimism_score`
- `q12_control_score`
- `q13_protocols_score`
- `q14_anxiety_score`
- Score ordinal final:
- `q15_wellbeing_score`

## 5. Calidad esperada
- Sin columnas de PII en `interim` y `processed`.
- Catalogos estandarizados por variable.
- Script reproducible sin pasos manuales.
