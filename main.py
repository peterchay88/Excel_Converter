import pandas as pd
import glob

filepath = glob.glob("invoices/*xlsx")

for file in filepath:
    df = pd.read_excel(file, sheet_name="Sheet 1")

    print(df)