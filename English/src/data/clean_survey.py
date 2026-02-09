from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import pandas as pd


LIKERT_LEVELS = ["Nunca", "Casi nunca", "De vez en cuando", "Casi siempre", "Siempre"]


COLUMN_RENAME = {
    "Marca temporal": "timestamp_raw",
    "Direccion de correo electronico": "email",
    "Direcci\u00f3n de correo electr\u00f3nico": "email",
    "Eres... (selecciona uno)": "gender",
    "Tu nombre": "name",
    "1.-\u00bfC\u00f3mo estas en este momento?": "q1_current_state",
    "2.-\u00bfC\u00f3mo te has sentido contigo mismo, en este confinamiento, hablando emocionalmente?": "q2_emotional_state",
    "3.-\u00bfEsta pandemia ha tenido impacto de manera positiva o negativa hacia ti?": "q3_impact",
    "4.-\u00bfHas tenido problemas sociales, emocionales, economicos o psicologicos en esta pandemia?": "q4_problems",
    "5.-Si la respuesta anterior fue si, \u00bfHas platicado con alguien o has buscado ayuda?": "q5_help_seek",
    "6.-\u00bfAntes del confinamiento por el COVID-19, como te sentias emocionalmente?Bien": "q6_pre_pandemic_state",
    "6.-\u00bfAntes del confinamiento por el COVID-19, como te sent\u00edas emocionalmente?Bien": "q6_pre_pandemic_state",
    "7.-\u00bfHas aprendido algo nuevo en este confinamiento? (Ya sea un nuevo idioma, artes marciales, manualidades, etc)": "q7_learned_new_skill",
    "8.-Si tu respuesta a la pregunta anterior fue si, comparte que fue lo que has aprendido, pueden ser 1 o varias.": "q8_learned_text",
    "9.-\u00bfHas pensado que las cosas volveran a ser como antes o se mantendra la nueva normalidad?": "q9_future_normality",
    "10.-\u00bfC\u00f3mo te sientes al final de todo? [Me he sentido nervioso o estresado por la epidemia]": "q10_stress",
    "11.-\u00bfC\u00f3mo te sientes al final de todo? [He sentido que las cosas van bien (optimista) con]": "q11_optimism",
    "12.-\u00bfC\u00f3mo te sientes al final de todo? [He sentido que tengo todo controlado en relaci\u00f3n con la pandemia]": "q12_control",
    "13.-\u00bfC\u00f3mo te sientes al final de todo? [Sigues los protocolos que el sistema de salud ha recomendado.]": "q13_protocols",
    "14.-\u00bfC\u00f3mo te sientes al final de todo? [Sufres ansiedad.]": "q14_anxiety",
    "15.-Por ultimo, siendo honestos, estas bien? ": "q15_wellbeing_final",
}


PII_COLUMNS = ["email", "name"]
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else (PROJECT_ROOT / path)


def rel_or_abs(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def canonical_col(name: object) -> str:
    text = str(name).strip().lower()
    text = "".join(
        ch for ch in unicodedata.normalize("NFKD", text) if not unicodedata.combining(ch)
    )
    text = re.sub(r"\s+", " ", text)
    return text


def normalize_text(value: object) -> object:
    if pd.isna(value):
        return pd.NA
    text = str(value).strip()
    text = re.sub(r"\s+", " ", text)
    return text if text else pd.NA


def normalize_basic(value: object) -> object:
    text = normalize_text(value)
    if pd.isna(text):
        return pd.NA

    replacements = {
        "Si": "Si",
        "S\u00ed": "Si",
        "Negativa.": "Negativa",
        "Positiva.": "Positiva",
        "Siempre.": "Siempre",
        "Mal.": "Mal",
    }
    return replacements.get(text, text)


def normalize_likert(value: object) -> object:
    text = normalize_basic(value)
    if pd.isna(text):
        return pd.NA

    raw_tokens = [token.strip(" .") for token in str(text).split(",")]
    canonical = {
        "nunca": "Nunca",
        "casi nunca": "Casi nunca",
        "de vez en cuando": "De vez en cuando",
        "casi siempre": "Casi siempre",
        "siempre": "Siempre",
    }
    for token in raw_tokens:
        key = token.lower()
        if key in canonical:
            return canonical[key]
    return text


def cast_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    if "timestamp_raw" not in df.columns:
        return df

    series = df["timestamp_raw"]
    # Google Forms exports may already be datetime; Excel exports may be serial numbers.
    if pd.api.types.is_numeric_dtype(series):
        df["timestamp"] = pd.to_datetime(series, errors="coerce", origin="1899-12-30", unit="D")
    else:
        df["timestamp"] = pd.to_datetime(series, errors="coerce")
    return df


def build_scores(df: pd.DataFrame) -> pd.DataFrame:
    likert_score = {
        "Nunca": 0,
        "Casi nunca": 1,
        "De vez en cuando": 2,
        "Casi siempre": 3,
        "Siempre": 4,
    }
    for col in ["q10_stress", "q11_optimism", "q12_control", "q13_protocols", "q14_anxiety"]:
        if col in df.columns:
            df[f"{col}_score"] = df[col].map(likert_score)

    wellbeing_score = {"No": 0, "Tal vez": 1, "Si": 2}
    if "q15_wellbeing_final" in df.columns:
        df["q15_wellbeing_score"] = df["q15_wellbeing_final"].map(wellbeing_score)

    return df


def load_and_clean(raw_file: Path) -> pd.DataFrame:
    df = pd.read_excel(raw_file, sheet_name="BD")
    df = df.dropna(how="all").copy()

    # Robust rename: canonicalize source headers to absorb accent and spacing variants.
    rename_map = {}
    canonical_target = {canonical_col(k): v for k, v in COLUMN_RENAME.items()}
    for col in df.columns:
        key = canonical_col(col)
        if key in canonical_target:
            rename_map[col] = canonical_target[key]
    df = df.rename(columns=rename_map)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].map(normalize_basic)

    df = cast_timestamp(df)

    likert_cols = ["q10_stress", "q11_optimism", "q12_control", "q13_protocols", "q14_anxiety"]
    for col in likert_cols:
        if col in df.columns:
            df[col] = df[col].map(normalize_likert)
            df[col] = pd.Categorical(df[col], categories=LIKERT_LEVELS, ordered=True)

    if "q3_impact" in df.columns:
        df["q3_impact"] = df["q3_impact"].replace({"Positiva.": "Positiva", "Negativa.": "Negativa"})

    if "q15_wellbeing_final" in df.columns:
        df["q15_wellbeing_final"] = df["q15_wellbeing_final"].replace({"S\u00ed": "Si"})

    df = df.drop(columns=[col for col in PII_COLUMNS if col in df.columns], errors="ignore")
    df = build_scores(df)
    return df


def safe_write(df: pd.DataFrame, output_parquet: Path, output_csv: Path) -> None:
    output_parquet.parent.mkdir(parents=True, exist_ok=True)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    try:
        df.to_parquet(output_parquet, index=False)
    except Exception:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean raw survey dataset.")
    parser.add_argument(
        "--raw-file",
        type=Path,
        default=Path("data/raw/survey_covid_2021.xlsx"),
        help="Path to raw Excel file.",
    )
    parser.add_argument(
        "--interim-parquet",
        type=Path,
        default=Path("data/interim/survey_clean_stage.parquet"),
        help="Path to interim parquet output.",
    )
    parser.add_argument(
        "--processed-parquet",
        type=Path,
        default=Path("data/processed/survey_analytics.parquet"),
        help="Path to processed parquet output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    raw_file = resolve_project_path(args.raw_file)
    interim_parquet = resolve_project_path(args.interim_parquet)
    processed_parquet = resolve_project_path(args.processed_parquet)
    interim_csv = PROJECT_ROOT / "data/interim/survey_clean_stage.csv"
    processed_csv = PROJECT_ROOT / "data/processed/survey_analytics.csv"

    cleaned = load_and_clean(raw_file)
    safe_write(cleaned, interim_parquet, interim_csv)
    safe_write(cleaned, processed_parquet, processed_csv)

    print(f"Rows: {len(cleaned)}")
    print(f"Columns: {len(cleaned.columns)}")
    print(f"Interim CSV: {rel_or_abs(interim_csv)}")
    print(f"Processed CSV: {rel_or_abs(processed_csv)}")


if __name__ == "__main__":
    main()
