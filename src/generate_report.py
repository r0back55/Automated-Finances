from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from pathlib import Path

def generate_report(summary_text: str):
    now = datetime.now().strftime("%Y_%m")
    report_path = Path(__file__).parent.parent / f"data/output/reports/{now}_report.pdf"

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(report_path, pagesize=A4)
    content = [Paragraph("Monthly Financial Report", styles["Title"]), Spacer(1, 12)]
    content.append(Paragraph(summary_text, styles["Normal"]))
    doc.build(content)
    print(f"✅ Report generated: {report_path}")
