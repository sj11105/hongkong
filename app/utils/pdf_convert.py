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

if __name__ == "__main__":
    sample_text = "## Meeting Summary: Type 2 Diabetes Risk Factors, Diagnosis, and Management\n\n**Topic Overview:** This meeting discussed type 2 diabetes, focusing on risk factors, diagnosis, and management strategies.  The discussion included a question from a viewer regarding a high sugar urine sample and its implications.  The importance of regular testing and healthy lifestyle choices was emphasized.\n\n**Key Action Points:**\n\n* **Risk Factors for Type 2 Diabetes:**  Participants should be aware of the following risk factors: age (over 40), family history (first-degree relatives with type 2 diabetes), ethnic background (Indigenous, Asian, South Asian, Hispanic, African), gestational diabetes history, delivering a baby over 9 pounds, polycystic ovarian syndrome, lack of exercise, and being overweight or obese.\n* **Diabetes Diagnosis:**  A high sugar content in a urine sample is not definitive for diabetes diagnosis.  Blood tests are the standard method for diagnosing diabetes.  Individuals should consult their doctor for proper testing.\n* **Signs and Symptoms of Diabetes:** Common symptoms include frequent urination, excessive thirst, weight changes, fatigue, and blurred vision.  Type 1 diabetes symptoms are typically rapid and dramatic, while type 2 diabetes symptoms can be gradual and unnoticed.  Many individuals with type 2 diabetes are unaware of their condition. Regular testing is crucial, especially for those with risk factors.\n* **Diabetes Testing Recommendations:**  Regular diabetes testing is recommended, particularly after age 40 (every 3 years).  More frequent testing (before age 40 or annually) is advised for individuals with additional risk factors.\n* **Long-Term Complications of Diabetes:**  The meeting highlighted serious long-term complications of diabetes, including increased risks of heart disease, kidney failure, blindness, and amputations.\n* **Diabetes Management and Prevention:** Proper diabetes management can prevent or delay these complications.  Key strategies emphasized include:\n    * **Healthy Food Choices:**  Adherence to dietary guidelines (e.g., Canada's Food Guide, available in multiple languages) is essential. This includes a balanced diet with diverse food groups, increased plant-based protein, healthy fats (olive, canola, soybean, sunflower oils), and limiting saturated fats, processed foods, added sodium, sugars, and saturated fats.\n    * **Hydration:**  Replacing sugary drinks with water is encouraged.\n    * **Food Label Awareness:** Paying attention to food labels and being mindful of marketing tactics is important.\n\n\n**Multilingual Aspects:** The transcript includes English and Chinese.  The Chinese portions mirror and expand upon the information provided in English, reinforcing key concepts and providing additional context.  Mention of the availability of the Canada Food Guide in Chinese, Hindi, and Gujarati highlights the effort to reach diverse populations.  The presence of additional languages beyond English and Chinese is noted but not fully analyzed due to limitations in available characters.\n"

    generate_summary_pdf(sample_text , "kmao.pdf")

