# Project Phases

## Phase 0 - Setup
- Define folder structure and dependencies.
- DoD: repository ready to run pipeline.

## Phase 1 - Raw
- Load and document original source.
- DoD: `data/raw/` is stable and immutable.

## Phase 2 - Cleaning (staging)
- Apply cleaning and standardization rules.
- DoD: normalized output in `data/interim/`.

## Phase 3 - Analytical dataset (mart)
- Generate derived variables and final dataset.
- DoD: `data/processed/` output ready for EDA/BI.

## Phase 4 - Analysis
- EDA, statistical testing, and interpretation.
- DoD: findings report in `reports/` with limitations.

## Phase 5 - Dashboard
- Build KPI layer and visualization interface.
- DoD: dashboard consumes only processed data.
