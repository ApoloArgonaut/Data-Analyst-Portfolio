# Findings Report - COVID Survey (2021)

## 1. Executive Summary
Este reporte resume los hallazgos principales del analisis exploratorio e inferencial sobre bienestar emocional durante el confinamiento.

Estado del reporte:
- Fecha de ejecucion: `2026-02-09`
- Fuente procesada: `data/processed/survey_analytics.csv`
- Version del notebook: `notebooks/01_eda.executed.ipynb`

## 2. Objetivo Analitico
- Entender la distribucion del bienestar reportado.
- Identificar asociaciones entre impacto/problemas y bienestar final.
- Evaluar senales relacionadas con ansiedad y riesgo de bajo bienestar.

## 3. Alcance y Fuente de Datos
- Dataset raw: `data/raw/survey_covid_2021.xlsx` (hoja `BD`)
- Unidad de analisis: respuesta individual.
- Tamano de muestra analizada: `178`
- Periodo de captura: `2021`

## 4. Calidad de Datos

### 4.1 Resumen de calidad
- Registros iniciales: `178`
- Registros finales: `178`
- Columnas eliminadas por PII: `email`, `name`
- Principales variables con nulos: `q8_learned_text`, `q5_help_seek`, `timestamp`

### 4.2 Reglas de limpieza aplicadas
- Normalizacion de catalogos textuales.
- Estandarizacion de escala Likert.
- Resolucion de respuestas compuestas en Likert.
- Generacion de variables de score ordinal.

Referencia tecnica: `docs/LIMPIEZA_RAW.md`

## 5. KPIs Principales

| KPI | Valor | Interpretacion breve |
|---|---:|---|
| Total de respuestas | `178` | Base de analisis final. |
| % impacto negativo percibido | `51.98%` | Leve predominio de percepcion negativa. |
| % impacto positivo percibido | `48.02%` | Grupo casi equivalente al negativo. |
| % reporta problemas (`q4 = Si`) | `67.23%` | Dos de cada tres reportan problemas en pandemia. |
| % bienestar final `Si` | `56.74%` | Mayoria declara estar bien al cierre. |
| % bienestar final `No/Tal vez` | `41.01%` | Bloque relevante de riesgo percibido. |

## 6. Hallazgos Descriptivos

### 6.1 Distribuciones relevantes
- Hallazgo 1: el impacto percibido esta casi dividido entre negativo (51.98%) y positivo (48.02%).
- Hallazgo 2: 67.23% reporta problemas sociales/emocionales/economicos/psicologicos.
- Hallazgo 3: 41.01% termina en `No` o `Tal vez` sobre bienestar final.

### 6.2 Cruces clave
- Cruce `gender` vs `q15_wellbeing_final`: en hombres, `Si` = 58.70%; en mujeres, `Si` = 55.29%. Mujeres muestran mayor `No` (14.12%) que hombres (6.52%).
- Cruce `q3_impact` vs `q15_wellbeing_final`: hay tendencia visual, pero sin evidencia estadistica fuerte en chi-cuadrada.
- Cruce `q4_problems` vs `q15_wellbeing_final`: asociacion marcada; quienes responden `No` en problemas concentran mas `Si` en bienestar final.

## 7. Evidencia Inferencial

### 7.1 Pruebas Chi-cuadrada

| Relacion evaluada | Chi2 | p-value | dof | n | Conclusion |
|---|---:|---:|---:|---:|---|
| `q3_impact` vs `q15_wellbeing_final` | `4.1786` | `0.2428` | `3` | `177` | No significativa (alpha=0.05). |
| `q4_problems` vs `q15_wellbeing_final` | `30.4174` | `0.000033` | `6` | `177` | Significativa; asociacion fuerte. |
| `q4_problems` vs `anxiety_high` | `6.7327` | `0.0345` | `2` | `177` | Significativa; asociacion moderada. |

Decision estadistica (alpha = 0.05):
- `No se rechaza H0` para `q3_impact` vs `q15_wellbeing_final`.
- `Se rechaza H0` para `q4_problems` vs `q15_wellbeing_final`.
- `Se rechaza H0` para `q4_problems` vs `anxiety_high`.

### 7.2 Correlaciones de Spearman (scores ordinales)

| Variable A | Variable B | Rho | p-value | n | Lectura |
|---|---|---:|---:|---:|---|
| `q11_optimism_score` | `q12_control_score` | `0.5204` | `1.57e-13` | `175` | Asociacion positiva alta. |
| `q14_anxiety_score` | `q15_wellbeing_score` | `-0.4633` | `1.55e-10` | `172` | Mayor ansiedad, menor bienestar final. |
| `q10_stress_score` | `q14_anxiety_score` | `0.3891` | `9.45e-08` | `176` | Estres y ansiedad crecen juntos. |
| `q10_stress_score` | `q15_wellbeing_score` | `-0.3777` | `2.78e-07` | `174` | Mayor estres, menor bienestar reportado. |

## 8. Modelo Logistico Exploratorio
Target:
- `target_low_wellbeing = 1` si `q15_wellbeing_final` en `{No, Tal vez}`.

Features usadas:
- Scores Likert (`q10` a `q14`), `q3_impact`, `q4_problems`, `gender` (si disponibles).

Resultados:
- Matriz de confusion: `[[17, 10], [2, 16]]` (filas reales `[0,1]`, columnas predichas `[0,1]`).
- Precision/Recall/F1 por clase:
- Clase `0` (no riesgo): `0.895 / 0.630 / 0.739`
- Clase `1` (riesgo bajo bienestar): `0.615 / 0.889 / 0.727`
- Accuracy global: `0.733` con `n_test=45`.
- Lectura ejecutiva: el modelo prioriza detectar casos de riesgo (recall alto en clase 1), a costa de falsos positivos moderados.

Nota:
- El modelo es exploratorio por tamano de muestra y contexto historico.

## 9. Conclusiones de Negocio
1. La variable mas determinante en esta muestra es `q4_problems`; su asociacion con bienestar final y ansiedad alta es estadisticamente significativa.
2. El riesgo percibido de bajo bienestar (No/Tal vez) alcanza 41.01%, por lo que no es un segmento marginal.
3. La evidencia ordinal sugiere un eje consistente: mas estres y ansiedad se vinculan con menor bienestar final.

## 10. Recomendaciones
1. Definir KPIs del dashboard sobre variables con mayor estabilidad y relevancia estadistica.
2. Evitar sobre-interpretacion causal; mantener lenguaje asociativo.
3. Proponer una nueva captura de datos para validar si patrones de 2021 persisten.

## 11. Limitaciones
- Muestra no probabilistica.
- Contexto temporal especifico de 2021.
- Posible sesgo de autopercepcion en respuestas.
- Algunas categorias pueden tener baja frecuencia.

## 12. Proximos Pasos
1. Consolidar visuales del notebook ejecutado en una version de reporte para portafolio.
2. Publicar visuales finales en dashboard desde `data/processed/`.
3. Preparar version ejecutiva corta para portafolio (`README` + highlights).
