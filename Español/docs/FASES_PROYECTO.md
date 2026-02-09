# Fases del Proyecto

## Fase 0 - Setup
- Estructura de carpetas y dependencias.
- DoD: repo listo para correr pipeline.

## Fase 1 - Raw
- Cargar y documentar fuente original.
- DoD: `data/raw/` estable e inmutable.

## Fase 2 - Limpieza (Staging)
- Aplicar reglas de limpieza y estandarizacion.
- DoD: salida en `data/interim/` con catalogos normalizados.

## Fase 3 - Dataset Analitico (Mart)
- Generar variables derivadas y dataset final.
- DoD: salida en `data/processed/` lista para EDA/BI.

## Fase 4 - Analisis
- EDA, pruebas estadisticas e interpretacion.
- DoD: reporte en `reports/` con hallazgos y limites.

## Fase 5 - Dashboard
- Construccion de KPIs y visualizacion.
- DoD: dashboard alimentado desde `processed`.
