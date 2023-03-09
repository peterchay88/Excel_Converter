import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoices/*xlsx")

for file in filepath:
    df = pd.read_excel(file, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(file).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(40, 10, f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(40, 10, f"Date: {date}")

    pdf.output(f"PDF/{invoice_nr}.pdf")