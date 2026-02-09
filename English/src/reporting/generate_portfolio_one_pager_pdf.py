from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "PORTAFOLIO_ONE_PAGER.pdf"


def wrap_text(text: str, font_name: str, font_size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        width = pdfmetrics.stringWidth(candidate, font_name, font_size)
        if width <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    max_width: float,
    font_name: str = "Helvetica",
    font_size: float = 10,
    leading: float = 13,
    bullet: bool = False,
) -> float:
    lines = wrap_text(text, font_name, font_size, max_width - (12 if bullet else 0))
    c.setFont(font_name, font_size)
    for idx, line in enumerate(lines):
        if bullet and idx == 0:
            c.drawString(x, y, "•")
            c.drawString(x + 12, y, line)
        elif bullet:
            c.drawString(x + 12, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y


def section_title(c: canvas.Canvas, title: str, x: float, y: float) -> float:
    c.setFillColor(colors.HexColor("#0B132B"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, title)
    return y - 15


def build_pdf(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=LETTER)
    w, h = LETTER

    margin = 0.7 * inch
    usable_w = w - 2 * margin
    y = h - margin

    # Header band
    c.setFillColor(colors.HexColor("#0B132B"))
    c.rect(0, h - 1.3 * inch, w, 1.3 * inch, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, h - 0.72 * inch, "Data Analyst Portfolio · One-Pager")
    c.setFont("Helvetica", 10.5)
    c.drawString(
        margin,
        h - 1.0 * inch,
        "Historical 2021 case transformed into a professional deliverable: pipeline, inference, and dashboard.",
    )

    y = h - 1.55 * inch

    # Two quick stat cards
    card_h = 0.72 * inch
    card_w = (usable_w - 0.2 * inch) / 2
    c.setFillColor(colors.HexColor("#ECF3F8"))
    c.roundRect(margin, y - card_h, card_w, card_h, 8, stroke=0, fill=1)
    c.roundRect(margin + card_w + 0.2 * inch, y - card_h, card_w, card_h, 8, stroke=0, fill=1)

    c.setFillColor(colors.HexColor("#0B132B"))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin + 12, y - 20, "Sample and context")
    c.setFont("Helvetica", 10)
    c.drawString(margin + 12, y - 36, "178 responses · 2021 · COVID-19 pandemic")
    c.drawString(margin + 12, y - 50, "Small non-probabilistic sample")

    x2 = margin + card_w + 0.2 * inch + 12
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x2, y - 20, "Impact and risk")
    c.setFont("Helvetica", 10)
    c.drawString(x2, y - 36, "67.23% reporting problems")
    c.drawString(x2, y - 50, "41.01% at-risk final wellbeing")

    y -= card_h + 0.28 * inch

    # Left / right columns
    gap = 0.28 * inch
    col_w = (usable_w - gap) / 2
    left_x = margin
    right_x = margin + col_w + gap

    # Left column: non-technical
    yl = y
    yl = section_title(c, "For general recruiters", left_x, yl)
    yl = draw_wrapped(
        c,
        "Turns noisy raw data into clear conclusions about emotional wellbeing and associated factors.",
        left_x,
        yl,
        col_w,
    )
    yl -= 6
    yl = draw_wrapped(c, "Perceived negative impact: 51.98%.", left_x, yl, col_w, bullet=True)
    yl = draw_wrapped(
        c,
        "Core finding: reporting problems is significantly associated with final wellbeing and anxiety.",
        left_x,
        yl,
        col_w,
        bullet=True,
    )
    yl = draw_wrapped(
        c,
        "Demonstrates structured thinking, communication, and decision orientation.",
        left_x,
        yl,
        col_w,
        bullet=True,
    )

    # Right column: technical
    yr = y
    yr = section_title(c, "For technical recruiters", right_x, yr)
    yr = draw_wrapped(c, "Stack: Python, pandas, scipy, scikit-learn, Jupyter, Streamlit.", right_x, yr, col_w)
    yr -= 6
    yr = draw_wrapped(c, "Reproducible pipeline: raw -> interim -> processed.", right_x, yr, col_w, bullet=True)
    yr = draw_wrapped(
        c,
        "Significant Chi-square tests: q4_problems vs q15 (p=0.000033), q4_problems vs anxiety_high (p=0.034516).",
        right_x,
        yr,
        col_w,
        bullet=True,
    )
    yr = draw_wrapped(c, "Exploratory logistic model: accuracy 0.733.", right_x, yr, col_w, bullet=True)

    y = min(yl, yr) - 10

    # Deliverables strip
    c.setFillColor(colors.HexColor("#F8F3EC"))
    c.roundRect(margin, y - 0.9 * inch, usable_w, 0.9 * inch, 8, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#0B132B"))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin + 12, y - 20, "Ready deliverables")
    c.setFont("Helvetica", 9.6)
    c.drawString(margin + 12, y - 36, "notebooks/00_resumen_ejecutivo.executed.ipynb")
    c.drawString(margin + 12, y - 50, "reports/findings.md  ·  app/streamlit_app.py")
    c.drawString(margin + 12, y - 64, "PORTAFOLIO_LANDING.md / PORTAFOLIO_LANDING.pdf")

    y -= 1.03 * inch

    # Disclaimer footer
    c.setFillColor(colors.HexColor("#3A506B"))
    c.setFont("Helvetica", 8.7)
    footer = (
        "Disclaimer: this case uses a historical (2021), non-probabilistic dataset. "
        "It should be interpreted as associative evidence and a demonstration of professional methodology."
    )
    y = draw_wrapped(c, footer, margin, y, usable_w, font_size=8.7, leading=11)

    c.showPage()
    c.save()


def main() -> None:
    build_pdf(OUTPUT_PATH)
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
