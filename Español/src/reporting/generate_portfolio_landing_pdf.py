from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def strip_md(line: str) -> str:
    text = line.replace("**", "").replace("`", "").replace("#", "").strip()
    return text


def build_pdf(input_md: Path, output_pdf: Path) -> None:
    lines = input_md.read_text(encoding="utf-8").splitlines()

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleLanding",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=12,
    )
    h2_style = ParagraphStyle(
        "Heading2Landing",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        spaceBefore=8,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "BodyLanding",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "BulletLanding",
        parent=body_style,
        leftIndent=14,
        bulletIndent=4,
    )
    code_style = ParagraphStyle(
        "CodeLanding",
        parent=body_style,
        fontName="Courier",
        fontSize=9.5,
        leading=12.5,
        leftIndent=10,
    )

    story = []
    in_code = False

    for raw in lines:
        line = raw.rstrip()

        if line.strip().startswith("```"):
            in_code = not in_code
            story.append(Spacer(1, 0.08 * inch))
            continue

        if in_code:
            story.append(Paragraph(line.replace(" ", "&nbsp;"), code_style))
            continue

        if not line.strip():
            story.append(Spacer(1, 0.06 * inch))
            continue

        if line.startswith("# "):
            story.append(Paragraph(strip_md(line[2:]), title_style))
            continue

        if line.startswith("## "):
            story.append(Paragraph(strip_md(line[3:]), h2_style))
            continue

        if line.startswith("- "):
            story.append(Paragraph(strip_md(line[2:]), bullet_style, bulletText="•"))
            continue

        story.append(Paragraph(strip_md(line), body_style))

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title="Portfolio Landing - Data Analyst Case",
    )
    doc.build(story)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate PDF from portfolio landing markdown.")
    parser.add_argument(
        "--input-md",
        type=Path,
        default=PROJECT_ROOT / "PORTAFOLIO_LANDING.md",
        help="Input markdown file.",
    )
    parser.add_argument(
        "--output-pdf",
        type=Path,
        default=PROJECT_ROOT / "PORTAFOLIO_LANDING.pdf",
        help="Output PDF file.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_pdf(args.input_md, args.output_pdf)
    print(f"PDF generated: {args.output_pdf}")


if __name__ == "__main__":
    main()
