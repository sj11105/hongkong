from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import re
import os 
import uuid


def markdown_to_html(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    return text


def generate_summary_pdf(summary_text: str, pdf_path: str):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        topMargin=20,   
        bottomMargin=30,
        leftMargin=40,
        rightMargin=40
    )
    styles = getSampleStyleSheet()
    story = []

    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        spaceAfter=6,
        fontSize=16,
        leading=18
    )
    subheading_style = ParagraphStyle(
        'Subheading',
        parent=styles['Heading2'],
        alignment=TA_LEFT,
        spaceAfter=4,
        fontSize=12.5,
        leading=15
    )
    para_style = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontSize=10.5,
        spaceAfter=4,
        leading=13
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=para_style,
        leftIndent=16,
        bulletIndent=6,
        spaceBefore=1,
        spaceAfter=1
    )

    lines = summary_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        if re.match(r"^#{2,}\s", line):  # Heading
            story.append(Paragraph(markdown_to_html(line.lstrip("# ").strip()), heading_style))
        elif re.match(r"^\*\*.+\*\*:$", line):  # Subheading
            story.append(Paragraph(markdown_to_html(line.strip()), subheading_style))
        elif re.match(r"^[-*]\s", line):  # Bullet
            bullets = []
            while i < len(lines) and re.match(r"^[-*]\s", lines[i].strip()):
                bullets.append(lines[i].strip()[2:].strip())
                i += 1
            bullet_paragraphs = [ListItem(Paragraph(markdown_to_html(b), bullet_style)) for b in bullets]
            story.append(ListFlowable(bullet_paragraphs, bulletType='bullet'))
            continue
        else:
            story.append(Paragraph(markdown_to_html(line), para_style))

        # Minimal spacing between items
        story.append(Spacer(1, 4))
        i += 1

    doc.build(story)
    print(f"PDF generated at {pdf_path}")


def save_summary_pdf_to_pdfhub(summary_text:str , audio_filename:str) -> str:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    APP_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
    PDF_DIR = os.path.join(APP_DIR, "pdfhub")
    os.makedirs(PDF_DIR, exist_ok=True)

    audio_uuid = audio_filename.split("_")[0]
    pdf_filename = f"{audio_uuid}_summary.pdf"
    pdf_path = os.path.join(PDF_DIR, pdf_filename)

    generate_summary_pdf(summary_text,pdf_path)
    return pdf_path


