# Parte Teorica del Proyecto

## 1. Contexto del caso
Este proyecto parte de una encuesta aplicada en 2021 sobre vida cotidiana y salud emocional durante el confinamiento por COVID-19.  
El material original existe en `data/raw/survey_covid_2021.xlsx` y conserva respuestas individuales de 178 personas.

El objetivo de esta fase teorica es convertir un trabajo academico previo en un proyecto de Data Analyst profesional, reproducible y defendible.

## 2. Problema de analisis
Aunque durante la pandemia hubo metricas epidemiologicas abundantes, el componente de bienestar emocional cotidiano suele estar menos estructurado en datos accionables.  
El problema analitico central es responder:

- Como se distribuye el estado emocional reportado en la muestra?
- Que variables se asocian con mayor senal de ansiedad?
- Que perfil de personas reporta bienestar final bajo o incierto?

## 3. Justificacion
- Valor tecnico: se crea un pipeline reproducible de datos reales.
- Valor metodologico: se documenta limpieza, sesgos y limites estadisticos.
- Valor de portafolio: permite mostrar calidad de analisis y no solo visualizacion.
- Valor aplicado: genera base para decisiones de apoyo emocional y comunicacion preventiva.

## 4. Objetivos

### 4.1 Objetivo general
Construir un flujo analitico en Python para limpiar, estructurar y analizar la encuesta, generando hallazgos claros sobre bienestar y ansiedad.

### 4.2 Objetivos especificos
- Estandarizar la base original en una tabla analitica limpia.
- Anonimizar datos sensibles (correo y nombre).
- Definir un diccionario de datos y reglas de calidad.
- Ejecutar analisis descriptivo e inferencial.
- Preparar dataset procesado para etapa de dashboard.

## 5. Preguntas de investigacion y supuestos

### 5.1 Preguntas principales
- Existe asociacion entre impacto percibido de la pandemia y bienestar final?
- Existe asociacion entre reportar problemas emocionales y reportar ansiedad frecuente?
- Cambia la distribucion de bienestar final por genero?

### 5.2 Hipotesis de trabajo (orientativas)
- H1: impacto negativo percibido se asocia con mayor probabilidad de responder `No` o `Tal vez` en bienestar final.
- H2: quienes reportan problemas emocionales/sociales/economicos/psicologicos muestran mayor frecuencia en niveles altos de ansiedad.
- H3: las variables tipo Likert de la seccion final pueden condensarse en un indice interpretable.

## 6. Marco conceptual y operacionalizacion

### 6.1 Unidades y temporalidad
- Unidad de analisis: una respuesta individual a encuesta.
- Corte temporal: transversal (un momento de captura, sin seguimiento longitudinal).

### 6.2 Variables clave
- Demografia minima: genero.
- Estado actual y estado previo del bienestar emocional.
- Impacto percibido de la pandemia.
- Reporte de problemas y busqueda de ayuda.
- Reactivos Likert de estres, optimismo, control, protocolos y ansiedad.
- Variable de salida principal: `q15_wellbeing_final`.

### 6.3 Escalas
- Nominal: genero, impacto, aprendizaje, busqueda de ayuda.
- Ordinal: respuestas tipo `Nunca` a `Siempre`.

## 7. Enfoque metodologico

### 7.1 Tipo de estudio
- Cuantitativo, observacional, transversal, no experimental.

### 7.2 Estrategia analitica
1. Depuracion y estandarizacion de catalogos.
2. Perfilado descriptivo de frecuencias y porcentajes.
3. Cruces bivariados y pruebas de asociacion.
4. Construccion de variables derivadas (scores ordinales e indice simple).
5. Modelado exploratorio para probabilidad de bienestar final bajo.

### 7.3 Pruebas y tecnicas sugeridas
- Chi-cuadrada para asociacion entre categoricas.
- Spearman para variables ordinales.
- Regresion logistica binaria (objetivo: `No/Tal vez` vs `Si`).
- Segmentacion exploratoria con clustering sobre variables codificadas.

## 8. Calidad de datos y sesgos esperados

### 8.1 Riesgos de calidad
- Variantes textuales para la misma categoria.
- Respuestas compuestas en reactivos Likert (ej. dos opciones en una celda).
- Nulos o `Prefiero no responder`.

### 8.2 Sesgos de estudio
- Muestra no probabilistica.
- Segmento etario y geografico acotado.
- Contexto historico especifico (2021).

### 8.3 Implicacion
Los resultados describen el comportamiento de esta muestra y no deben extrapolarse de forma fuerte a toda la poblacion.

## 9. Gobierno de datos y etica
- Remover o anonimizar identificadores directos.
- Mantener `raw` inmutable y versionar transformaciones.
- Reportar limites metodologicos en hallazgos.
- No publicar datos sensibles en dashboard.

## 10. Arquitectura por fases

### Fase 0 - Discovery
- Revisar fuentes y estructura.
- Confirmar definiciones de variables.

### Fase 1 - Raw Data
- Ubicar fuente original en `data/raw/`.
- Documentar procedencia y reglas de no edicion.

### Fase 2 - Staging / Limpieza
- Aplicar reglas de normalizacion.
- Resolver categorias inconsistentes.
- Crear tabla intermedia reproducible.

### Fase 3 - Analitica (Mart)
- Generar dataset procesado listo para analisis y BI.
- Construir variables derivadas.

### Fase 4 - EDA e inferencia
- Descriptivo, pruebas, modelo exploratorio y reporte.

### Fase 5 - Dashboard (posterior)
- Solo iniciar cuando la calidad y trazabilidad de datos sea estable.

## 11. Criterios para pasar a dashboard
- Dataset limpio y documentado en `data/processed/`.
- Catalogo de KPIs definido y validado.
- Reglas de limpieza auditables.
- Hallazgos estadisticos con limites claramente declarados.

## 12. Entregables teoricos que deben existir
- `PARTE_TEORICA_PROYECTO.md` (este documento).
- `PLAN_PROYECTO_ANALYST.md` (plan operativo ejecutable).
- `docs/LIMPIEZA_RAW.md` (reglas de transformacion).
- `docs/FASES_PROYECTO.md` (control por fases y Definition of Done).
