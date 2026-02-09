# Plan Operativo del Proyecto (Combinado con Parte Teorica)

Este plan ejecuta lo definido en `PARTE_TEORICA_PROYECTO.md` y lo traduce a fases tecnicas concretas.

## 1. Alcance del MVP (antes de dashboard)
- Ingesta reproducible del archivo raw.
- Limpieza estandar con reglas documentadas.
- Dataset analitico procesado para EDA e inferencia.
- Documentacion de calidad y supuestos.

## 2. Estructura de carpetas por fases

```text
data/
  raw/        # fuente original inmutable
  interim/    # salida de limpieza intermedia
  processed/  # dataset final para analisis y BI
docs/
  FASES_PROYECTO.md
  LIMPIEZA_RAW.md
src/
  data/
    clean_survey.py
notebooks/
reports/
```

## 3. Fases de ejecucion

### Fase 0 - Setup
- Crear estructura del repositorio.
- Definir dependencias en `requirements.txt`.

Definition of Done:
- Estructura base creada y versionada.

### Fase 1 - Raw Data
- Guardar dataset original en `data/raw/survey_covid_2021.xlsx`.
- Documentar procedencia y politica de inmutabilidad.

Definition of Done:
- Fuente raw identificada, trazable y sin modificaciones directas.

### Fase 2 - Limpieza / Staging
- Estandarizar nombres de columnas.
- Eliminar PII (correo y nombre).
- Normalizar catalogos de respuestas.
- Resolver respuestas compuestas de Likert.
- Guardar salida en `data/interim/`.

Definition of Done:
- Script ejecutable y reglas de limpieza documentadas.

### Fase 3 - Dataset Analitico
- Crear columnas derivadas (scores ordinales).
- Guardar salida final en `data/processed/`.

Definition of Done:
- Dataset listo para EDA, pruebas estadisticas y BI.

### Fase 4 - Analisis
- EDA descriptivo.
- Pruebas de asociacion (chi-cuadrada, Spearman).
- Modelo exploratorio (logistica).

Definition of Done:
- Reporte con hallazgos, supuestos y limitaciones.

### Fase 5 - Dashboard (posterior)
- Diseno de KPIs y visuales con base en datos confiables.

Definition of Done:
- Dashboard alimentado solo desde `data/processed/`.

## 4. Entregables obligatorios
- `PARTE_TEORICA_PROYECTO.md`
- `PLAN_PROYECTO_ANALYST.md`
- `docs/FASES_PROYECTO.md`
- `docs/LIMPIEZA_RAW.md`
- `src/data/clean_survey.py`
- `data/interim/` y `data/processed/` con salidas del pipeline

## 5. Criterios de calidad
- Reproducibilidad: mismo input raw produce mismo output.
- Trazabilidad: cada transformacion esta en script y documento.
- Transparencia: limites y sesgos explicitados.
- Seguridad: sin PII en salidas para analisis/dashboard.

## 6. Siguiente ejecucion recomendada
1. Instalar dependencias.
2. Ejecutar script de limpieza.
3. Validar salida en `interim` y `processed`.
4. Arrancar notebook de EDA.
