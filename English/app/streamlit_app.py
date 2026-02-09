from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy.stats import chi2_contingency


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data/processed/survey_analytics.csv"
COLORWAY = ["#0B132B", "#1C2541", "#3A506B", "#5BC0BE", "#F4A259", "#E07A5F"]


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

        :root {
            --ink: #0b132b;
            --ink-soft: #3a506b;
            --teal: #5bc0be;
            --orange: #f4a259;
            --paper: #f9fbfd;
        }

        .stApp {
            background: radial-gradient(1000px 400px at 0% 0%, rgba(91,192,190,.18), rgba(91,192,190,0) 60%),
                        radial-gradient(900px 500px at 100% 0%, rgba(244,162,89,.15), rgba(244,162,89,0) 55%),
                        var(--paper);
            color: var(--ink);
            font-family: "IBM Plex Sans", sans-serif;
        }

        h1, h2, h3 {
            font-family: "Space Grotesk", sans-serif !important;
            letter-spacing: -0.02em;
        }

        .hero-card {
            border: 1px solid rgba(11,19,43,.12);
            border-radius: 18px;
            padding: 18px 20px;
            background: rgba(255,255,255,.9);
            box-shadow: 0 8px 30px rgba(11,19,43,.06);
            animation: fadein .5s ease-out;
        }

        .hero-kicker {
            font-size: .82rem;
            color: var(--ink-soft);
            text-transform: uppercase;
            letter-spacing: .08em;
            margin-bottom: .3rem;
        }

        .hero-title {
            font-size: 1.6rem;
            font-weight: 700;
            margin: 0;
            color: var(--ink);
        }

        .hero-sub {
            margin-top: .45rem;
            color: var(--ink-soft);
        }

        @keyframes fadein {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(show_spinner=False)
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    replace_map = {
        "Si": "Si",
        "S\u00ed": "Si",
        "Negativa.": "Negativa",
        "Positiva.": "Positiva",
        "Siempre.": "Siempre",
    }
    for col in ["q3_impact", "q4_problems", "q15_wellbeing_final", "q10_stress", "q14_anxiety"]:
        if col in df.columns:
            df[col] = df[col].replace(replace_map)

    return df


def pct(mask: pd.Series) -> float:
    if len(mask) == 0:
        return float("nan")
    return round(mask.mean() * 100, 2)


def chi_square(df: pd.DataFrame, a: str, b: str) -> dict[str, float | int | str]:
    sub = df[[a, b]].dropna()
    table = pd.crosstab(sub[a], sub[b])
    if table.shape[0] < 2 or table.shape[1] < 2:
        return {"test": f"{a} vs {b}", "chi2": np.nan, "p_value": np.nan, "dof": np.nan, "n": len(sub)}
    chi2, p_val, dof, _ = chi2_contingency(table)
    return {"test": f"{a} vs {b}", "chi2": chi2, "p_value": p_val, "dof": dof, "n": len(sub)}


def main() -> None:
    st.set_page_config(page_title="COVID Wellbeing Dashboard", page_icon=":bar_chart:", layout="wide")
    inject_styles()

    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">Phase 5 · Dashboard</div>
            <p class="hero-title">Emotional impact of lockdown (2021 sample)</p>
            <p class="hero-sub">Analytical dashboard on wellbeing, anxiety, and associated factors. Source: 178 survey responses.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.warning(
        "Important disclaimer: this information was collected in 2021, during the peak of the COVID-19 pandemic, "
        "using a small non-probabilistic sample. "
        "It is reused as a realistic portfolio case to demonstrate a professional Data Analyst workflow."
    )

    st.info(
        "Executive snapshot: 178 responses analyzed (2021). "
        "Negative impact 51.98%, problem reporting 67.23%, and 41.01% at-risk final wellbeing (No/Tal vez)."
    )

    if not DATA_PATH.exists():
        st.error("`data/processed/survey_analytics.csv` not found. Run first: `python src/data/clean_survey.py`")
        st.stop()

    df = load_data(DATA_PATH)
    base_n = len(df)

    st.sidebar.header("Filters")
    genders = sorted(df["gender"].dropna().unique().tolist()) if "gender" in df.columns else []
    impacts = sorted(df["q3_impact"].dropna().unique().tolist()) if "q3_impact" in df.columns else []
    wellbeings = (
        sorted(df["q15_wellbeing_final"].dropna().unique().tolist()) if "q15_wellbeing_final" in df.columns else []
    )

    sel_gender = st.sidebar.multiselect("Gender", options=genders, default=genders)
    sel_impact = st.sidebar.multiselect("Perceived impact", options=impacts, default=impacts)
    sel_wellbeing = st.sidebar.multiselect("Final wellbeing", options=wellbeings, default=wellbeings)

    filtered = df.copy()
    if sel_gender and "gender" in filtered.columns:
        filtered = filtered[filtered["gender"].isin(sel_gender)]
    if sel_impact and "q3_impact" in filtered.columns:
        filtered = filtered[filtered["q3_impact"].isin(sel_impact)]
    if sel_wellbeing and "q15_wellbeing_final" in filtered.columns:
        filtered = filtered[filtered["q15_wellbeing_final"].isin(sel_wellbeing)]

    if "timestamp" in filtered.columns and filtered["timestamp"].notna().any():
        min_d = filtered["timestamp"].min().date()
        max_d = filtered["timestamp"].max().date()
        date_window = st.sidebar.date_input("Date range", value=(min_d, max_d), min_value=min_d, max_value=max_d)
        if isinstance(date_window, tuple) and len(date_window) == 2:
            start_d, end_d = date_window
            filtered = filtered[
                (filtered["timestamp"].dt.date >= start_d) & (filtered["timestamp"].dt.date <= end_d)
            ]

    st.sidebar.caption(f"Filtered records: {len(filtered)} of {base_n}")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Responses", f"{len(filtered)}")
    col2.metric("% Negative impact", f"{pct(filtered['q3_impact'].eq('Negativa')):.2f}%" if "q3_impact" in filtered else "NA")
    col3.metric("% Reporting problems", f"{pct(filtered['q4_problems'].eq('Si')):.2f}%" if "q4_problems" in filtered else "NA")
    low_mask = filtered["q15_wellbeing_final"].isin(["No", "Tal vez"]) if "q15_wellbeing_final" in filtered else pd.Series([], dtype=bool)
    col4.metric("% At-risk wellbeing", f"{pct(low_mask):.2f}%")
    if "q14_anxiety_score" in filtered.columns:
        col5.metric("% High anxiety", f"{pct(filtered['q14_anxiety_score'].ge(3)):.2f}%")
    else:
        col5.metric("% High anxiety", "NA")

    st.markdown("## Overview")
    c1, c2 = st.columns(2)

    if "q3_impact" in filtered.columns:
        impact_count = filtered["q3_impact"].fillna("No data").value_counts().reset_index()
        impact_count.columns = ["Impact", "Count"]
        fig_impact = px.bar(
            impact_count,
            x="Impact",
            y="Count",
            color="Impact",
            color_discrete_sequence=COLORWAY,
            title="Perceived pandemic impact",
        )
        fig_impact.update_layout(showlegend=False, height=380)
        c1.plotly_chart(fig_impact, use_container_width=True)

    if "q15_wellbeing_final" in filtered.columns:
        order = ["No", "Tal vez", "Si", "Prefiero no responder."]
        wellbeing = filtered["q15_wellbeing_final"].fillna("No data")
        wellbeing_count = wellbeing.value_counts().reindex(order + ["No data"], fill_value=0).reset_index()
        wellbeing_count.columns = ["Final wellbeing", "Count"]
        fig_w = px.bar(
            wellbeing_count,
            x="Final wellbeing",
            y="Count",
            color="Final wellbeing",
            color_discrete_sequence=COLORWAY,
            title="Final reported wellbeing",
        )
        fig_w.update_layout(showlegend=False, height=380)
        c2.plotly_chart(fig_w, use_container_width=True)

    st.markdown("## Key Cross-Analysis")
    c3, c4 = st.columns(2)

    if {"gender", "q15_wellbeing_final"}.issubset(filtered.columns):
        ctab = pd.crosstab(filtered["gender"], filtered["q15_wellbeing_final"], normalize="index")
        fig_stack = go.Figure()
        for i, col in enumerate(ctab.columns):
            fig_stack.add_trace(
                go.Bar(
                    x=ctab.index,
                    y=ctab[col],
                    name=col,
                    marker_color=COLORWAY[i % len(COLORWAY)],
                )
            )
        fig_stack.update_layout(
            barmode="stack",
            title="Final wellbeing by gender (proportion)",
            yaxis_tickformat=".0%",
            height=420,
        )
        c3.plotly_chart(fig_stack, use_container_width=True)

    if {"q4_problems", "q15_wellbeing_final"}.issubset(filtered.columns):
        heat_df = pd.crosstab(filtered["q4_problems"], filtered["q15_wellbeing_final"])
        fig_heat = px.imshow(
            heat_df,
            text_auto=True,
            aspect="auto",
            color_continuous_scale=[[0, "#F4F7FB"], [1, "#0B132B"]],
            title="Count: reported problems vs final wellbeing",
        )
        fig_heat.update_layout(height=420)
        c4.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("## Emotional Scores")
    score_cols = [
        "q10_stress_score",
        "q11_optimism_score",
        "q12_control_score",
        "q13_protocols_score",
        "q14_anxiety_score",
    ]
    score_cols = [c for c in score_cols if c in filtered.columns]
    if score_cols:
        mean_scores = filtered[score_cols].mean().round(2).reset_index()
        mean_scores.columns = ["Variable", "Average"]
        fig_scores = px.bar(
            mean_scores,
            x="Variable",
            y="Average",
            color="Variable",
            color_discrete_sequence=COLORWAY,
            title="Average score by indicator (0 to 4)",
        )
        fig_scores.update_layout(showlegend=False, yaxis_range=[0, 4], height=360)
        st.plotly_chart(fig_scores, use_container_width=True)

    st.markdown("## Statistical Evidence (quick view)")
    test_rows: list[dict[str, float | int | str]] = []
    if {"q3_impact", "q15_wellbeing_final"}.issubset(filtered.columns):
        test_rows.append(chi_square(filtered, "q3_impact", "q15_wellbeing_final"))
    if {"q4_problems", "q15_wellbeing_final"}.issubset(filtered.columns):
        test_rows.append(chi_square(filtered, "q4_problems", "q15_wellbeing_final"))
    if {"q4_problems", "q14_anxiety_score"}.issubset(filtered.columns):
        tmp = filtered.copy()
        tmp["anxiety_high"] = np.where(tmp["q14_anxiety_score"] >= 3, "High", "Not high")
        test_rows.append(chi_square(tmp, "q4_problems", "anxiety_high"))

    if test_rows:
        tests_df = pd.DataFrame(test_rows)
        tests_df["significant_alpha_0_05"] = tests_df["p_value"] < 0.05
        st.dataframe(tests_df, use_container_width=True, hide_index=True)

    st.markdown("## Export")
    csv_data = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download filtered data (CSV)",
        data=csv_data,
        file_name="survey_filtered_dashboard.csv",
        mime="text/csv",
    )

    st.caption(
        "Methodological note: non-probabilistic sample and 2021 time context. "
        "Interpret results as associations, not causality."
    )


if __name__ == "__main__":
    main()
