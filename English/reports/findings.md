# Findings Report - COVID Survey (2021)

## 1. Executive summary
This report summarizes key findings from exploratory and inferential analysis of emotional wellbeing during lockdown.

Report status:
- Execution date: `2026-02-09`
- Processed source: `data/processed/survey_analytics.csv`
- Notebook version: `notebooks/01_eda.executed.ipynb`

## 2. Analytical objective
- Understand final wellbeing distribution.
- Identify associations between perceived impact/problems and final wellbeing.
- Evaluate anxiety-related signals connected to low wellbeing risk.

## 3. Scope and data source
- Raw dataset: `data/raw/survey_covid_2021.xlsx` (`BD` sheet)
- Unit of analysis: one survey response.
- Sample size analyzed: `178`
- Capture period: `2021`

## 4. Data quality

### 4.1 Quality summary
- Initial records: `178`
- Final records: `178`
- Removed PII columns: `email`, `name`
- Main variables with nulls: `q8_learned_text`, `q5_help_seek`, `timestamp`

### 4.2 Applied cleaning rules
- Text catalog normalization.
- Likert scale standardization.
- Combined Likert response handling.
- Derived ordinal score generation.

Technical reference: `docs/LIMPIEZA_RAW.md`

## 5. Main KPIs

| KPI | Value | Brief interpretation |
|---|---:|---|
| Total responses | `178` | Final analytical base. |
| % perceived negative impact | `51.98%` | Slight predominance of negative perception. |
| % perceived positive impact | `48.02%` | Nearly balanced against negative impact. |
| % reporting problems (`q4 = Si`) | `67.23%` | Roughly two out of three respondents report problems. |
| % final wellbeing `Si` | `56.74%` | Majority reports being okay at the end. |
| % final wellbeing `No/Tal vez` | `41.01%` | Meaningful at-risk wellbeing segment. |

## 6. Descriptive findings

### 6.1 Relevant distributions
- Finding 1: perceived impact is almost split between negative (51.98%) and positive (48.02%).
- Finding 2: 67.23% report social/emotional/economic/psychological problems.
- Finding 3: 41.01% end in `No` or `Tal vez` final wellbeing.

### 6.2 Key cross-tabs
- `gender` vs `q15_wellbeing_final`: men `Si` = 58.70%; women `Si` = 55.29%. Women show higher `No` (14.12%) than men (6.52%).
- `q3_impact` vs `q15_wellbeing_final`: visual trend exists, but no strong statistical evidence via Chi-square.
- `q4_problems` vs `q15_wellbeing_final`: marked association; respondents with `No` in problems concentrate more `Si` in final wellbeing.

## 7. Inferential evidence

### 7.1 Chi-square tests

| Tested relationship | Chi2 | p-value | dof | n | Conclusion |
|---|---:|---:|---:|---:|---|
| `q3_impact` vs `q15_wellbeing_final` | `4.1786` | `0.2428` | `3` | `177` | Not significant (alpha=0.05). |
| `q4_problems` vs `q15_wellbeing_final` | `30.4174` | `0.000033` | `6` | `177` | Significant; strong association. |
| `q4_problems` vs `anxiety_high` | `6.7327` | `0.0345` | `2` | `177` | Significant; moderate association. |

Statistical decision (alpha = 0.05):
- Fail to reject H0 for `q3_impact` vs `q15_wellbeing_final`.
- Reject H0 for `q4_problems` vs `q15_wellbeing_final`.
- Reject H0 for `q4_problems` vs `anxiety_high`.

### 7.2 Spearman correlations (ordinal scores)

| Variable A | Variable B | Rho | p-value | n | Reading |
|---|---|---:|---:|---:|---|
| `q11_optimism_score` | `q12_control_score` | `0.5204` | `1.57e-13` | `175` | Strong positive association. |
| `q14_anxiety_score` | `q15_wellbeing_score` | `-0.4633` | `1.55e-10` | `172` | Higher anxiety links to lower final wellbeing. |
| `q10_stress_score` | `q14_anxiety_score` | `0.3891` | `9.45e-08` | `176` | Stress and anxiety rise together. |
| `q10_stress_score` | `q15_wellbeing_score` | `-0.3777` | `2.78e-07` | `174` | Higher stress links to lower wellbeing. |

## 8. Exploratory logistic model
Target:
- `target_low_wellbeing = 1` when `q15_wellbeing_final` is in `{No, Tal vez}`.

Used features:
- Likert scores (`q10` to `q14`), `q3_impact`, `q4_problems`, `gender` (when available).

Results:
- Confusion matrix: `[[17, 10], [2, 16]]` (rows true `[0,1]`, cols predicted `[0,1]`).
- Precision/Recall/F1:
- Class `0` (lower risk): `0.895 / 0.630 / 0.739`
- Class `1` (at-risk wellbeing): `0.615 / 0.889 / 0.727`
- Global accuracy: `0.733` with `n_test=45`.
- Executive interpretation: the model prioritizes detection of at-risk cases (high class-1 recall), with moderate false positives.

Note:
- This model is exploratory, given sample size and historical context.

## 9. Business conclusions
1. The strongest driver in this sample is `q4_problems`; its association with final wellbeing and high anxiety is statistically significant.
2. At-risk final wellbeing (`No/Tal vez`) reaches 41.01%, so it is not a marginal group.
3. Ordinal evidence shows a coherent axis: higher stress/anxiety is linked to lower final wellbeing.

## 10. Recommendations
1. Build dashboard KPIs around stable, statistically relevant variables.
2. Avoid causal language; keep interpretation associative.
3. Consider a new data collection wave to test whether 2021 patterns persist.

## 11. Limitations
- Non-probabilistic sample.
- Time-specific context (2021).
- Possible self-perception bias in responses.
- Some categories may have low frequency.

## 12. Next steps
1. Consolidate final visuals from executed notebooks into portfolio-ready assets.
2. Publish final dashboard visuals using `data/processed/`.
3. Keep a short executive version for portfolio first-pass review.
