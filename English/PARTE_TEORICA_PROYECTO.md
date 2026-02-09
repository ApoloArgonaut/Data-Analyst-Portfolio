# Theoretical Project Section

## 1. Case context
This project is based on a 2021 survey about daily life and emotional wellbeing during COVID-19 lockdown.  
The source file is `data/raw/survey_covid_2021.xlsx`, containing 178 individual responses.

The purpose of this theoretical section is to transform an academic assignment into a professional, reproducible, and defensible Data Analyst project.

## 2. Analytical problem
During the pandemic, epidemiological metrics were widely available, but structured emotional wellbeing data was less common.  
The core analytical problem is:

- How is emotional state distributed in this sample?
- Which variables are associated with stronger anxiety signals?
- Which profiles report lower or uncertain final wellbeing?

## 3. Justification
- Technical value: reproducible pipeline on real data.
- Methodological value: explicit cleaning, bias handling, and statistical limits.
- Portfolio value: demonstrates end-to-end analysis quality, not only visualization.
- Practical value: provides a framework for emotional support and preventive communication insights.

## 4. Objectives

### 4.1 General objective
Build a Python analytical workflow to clean, structure, and analyze the survey, producing clear insights on wellbeing and anxiety.

### 4.2 Specific objectives
- Standardize the original dataset into a clean analytical table.
- Anonymize sensitive fields (email and name).
- Define a data dictionary and quality rules.
- Run descriptive and inferential analysis.
- Prepare processed data for dashboard consumption.

## 5. Research questions and assumptions

### 5.1 Main questions
- Is perceived pandemic impact associated with final wellbeing?
- Is reporting emotional/social/economic/psychological problems associated with frequent anxiety?
- Does final wellbeing distribution vary by gender?

### 5.2 Working hypotheses
- H1: perceived negative impact increases the probability of `No` or `Tal vez` in final wellbeing.
- H2: respondents reporting problems show higher frequency of high-anxiety levels.
- H3: final Likert items can be condensed into interpretable indices.

## 6. Conceptual framework and operationalization

### 6.1 Units and temporal design
- Unit of analysis: one survey response.
- Temporal design: cross-sectional (single capture window, no longitudinal tracking).

### 6.2 Key variables
- Basic demographics: gender.
- Current and pre-pandemic emotional states.
- Perceived pandemic impact.
- Problem reporting and help-seeking behavior.
- Likert items for stress, optimism, control, protocol adherence, and anxiety.
- Main outcome: `q15_wellbeing_final`.

### 6.3 Scales
- Nominal: gender, impact, learning, help-seeking.
- Ordinal: frequency answers from `Nunca` to `Siempre`.

## 7. Methodological approach

### 7.1 Study type
- Quantitative, observational, cross-sectional, non-experimental.

### 7.2 Analytical strategy
1. Catalog cleaning and standardization.
2. Descriptive profiling (frequencies and percentages).
3. Bivariate analysis and association tests.
4. Derived variables (ordinal scores and simple indices).
5. Exploratory modeling for low final wellbeing probability.

### 7.3 Suggested tests and techniques
- Chi-square for categorical association.
- Spearman for ordinal variables.
- Binary logistic regression (`No/Tal vez` vs `Si`).
- Exploratory clustering for risk-profile segmentation.

## 8. Data quality and expected bias

### 8.1 Quality risks
- Text variants for the same category.
- Combined responses in single Likert cells.
- Missing values and `Prefiero no responder`.

### 8.2 Study biases
- Non-probabilistic sample.
- Narrow age/geographic scope.
- Historical context restricted to 2021.

### 8.3 Implication
Results describe this sample and should not be strongly generalized to the full population.

## 9. Data governance and ethics
- Remove or anonymize direct identifiers.
- Keep `raw` immutable and version transformations.
- Explicitly report methodological limits.
- Avoid publishing sensitive data in dashboards.

## 10. Phase architecture

### Phase 0 - Discovery
- Review sources and structure.
- Confirm variable definitions.

### Phase 1 - Raw data
- Place original source in `data/raw/`.
- Document origin and no-edit policy.

### Phase 2 - Staging / Cleaning
- Apply normalization rules.
- Resolve inconsistent categories.
- Create reproducible intermediate table.

### Phase 3 - Analytics mart
- Build processed analytical dataset for analysis and BI.
- Create derived variables.

### Phase 4 - EDA and inference
- Descriptive analysis, statistical testing, exploratory modeling, and reporting.

### Phase 5 - Dashboard
- Start only after data quality and transformation traceability are stable.

## 11. Criteria to move into dashboard
- Clean documented dataset in `data/processed/`.
- Defined and validated KPI set.
- Auditable cleaning rules.
- Statistically supported findings with explicit limits.

## 12. Required theoretical deliverables
- `PARTE_TEORICA_PROYECTO.md` (this file, English content).
- `PLAN_PROYECTO_ANALYST.md` (operational project plan).
- `docs/LIMPIEZA_RAW.md` (cleaning rules).
- `docs/FASES_PROYECTO.md` (phase control and Definition of Done).
