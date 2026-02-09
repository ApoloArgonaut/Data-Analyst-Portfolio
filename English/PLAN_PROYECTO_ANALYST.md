# Operational Project Plan (Aligned with Theory)

This plan translates `PARTE_TEORICA_PROYECTO.md` into concrete execution phases.

## 1. MVP scope (before dashboard)
- Reproducible ingestion from raw source.
- Standardized cleaning with documented rules.
- Processed analytical dataset for EDA and inference.
- Explicit quality assumptions and limitations.

## 2. Phase-based folder structure

```text
data/
  raw/        # immutable original source
  interim/    # cleaned intermediate output
  processed/  # final dataset for analysis/BI
docs/
  FASES_PROYECTO.md
  LIMPIEZA_RAW.md
src/
  data/
    clean_survey.py
notebooks/
reports/
```

## 3. Execution phases

### Phase 0 - Setup
- Build repository structure.
- Define dependencies in `requirements.txt`.

Definition of Done:
- Base structure created and versioned.

### Phase 1 - Raw data
- Store original dataset in `data/raw/survey_covid_2021.xlsx`.
- Document provenance and immutability policy.

Definition of Done:
- Raw source is identified, traceable, and unchanged.

### Phase 2 - Cleaning / staging
- Standardize column names.
- Remove PII (email and name).
- Normalize answer catalogs.
- Resolve combined Likert responses.
- Save staging output in `data/interim/`.

Definition of Done:
- Executable cleaning script + documented cleaning rules.

### Phase 3 - Analytical dataset
- Create derived columns (ordinal scores).
- Save final output in `data/processed/`.

Definition of Done:
- Dataset ready for EDA, statistical testing, and BI.

### Phase 4 - Analysis
- Descriptive EDA.
- Association testing (Chi-square, Spearman).
- Exploratory logistic model.

Definition of Done:
- Findings report with assumptions and limitations.

### Phase 5 - Dashboard
- Build KPIs and visuals using validated processed data.

Definition of Done:
- Dashboard powered only by `data/processed/`.

## 4. Required deliverables
- `PARTE_TEORICA_PROYECTO.md`
- `PLAN_PROYECTO_ANALYST.md`
- `docs/FASES_PROYECTO.md`
- `docs/LIMPIEZA_RAW.md`
- `src/data/clean_survey.py`
- `data/interim/` and `data/processed/` pipeline outputs

## 5. Quality criteria
- Reproducibility: same raw input, same output.
- Traceability: every transformation documented in code and docs.
- Transparency: explicit assumptions and methodological limits.
- Data safety: no PII in analysis/dashboard outputs.

## 6. Recommended next execution
1. Install dependencies.
2. Run cleaning script.
3. Validate outputs in `interim` and `processed`.
4. Run EDA notebook.
