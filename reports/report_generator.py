from fpdf import FPDF
from pathlib import Path

def generate_report(config, rebalance, expenses, simulation, fig_path):
    """Generuje raport PDF podsumowujący analizy finansowe."""
    pdf = FPDF()
    pdf.add_page()

    # Dodanie Unicode font
    font_path = Path("fonts/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "", str(font_path), uni=True)
    pdf.set_font("DejaVu", "", 16)

    pdf.cell(0, 10, "Miesięczny raport finansowy", ln=True, align="C")

    pdf.set_font("DejaVu", "", 12)
    pdf.cell(0, 10, "1. Rebalancing portfela", ln=True)
    for _, row in rebalance.iterrows():
        pdf.cell(0, 8, f"{row['asset']}: {row['difference']:.2%} różnicy", ln=True)

    pdf.cell(0, 10, "", ln=True)
    pdf.cell(0, 10, "2. Wydatki", ln=True)
    pdf.cell(0, 8, f"Łączne wydatki: {expenses['total_expenses']:.2f} zł", ln=True)
    pdf.cell(0, 8, f"Limit: {expenses['limit']} zł", ln=True)
    pdf.cell(0, 8, f"Przekroczono limit: {'TAK' if expenses['alert'] else 'NIE'}", ln=True)

    pdf.cell(0, 10, "", ln=True)
    pdf.cell(0, 10, "3. Symulacja inwestycyjna", ln=True)
    pdf.cell(0, 8, f"Prognozowana wartość końcowa: {simulation['final_balance']:.2f} zł", ln=True)

    pdf.image(fig_path, x=10, y=pdf.get_y() + 5, w=180)
    output_path = Path(config['report']['output_dir']) / 'monthly_report.pdf'
    pdf.output(str(output_path))
