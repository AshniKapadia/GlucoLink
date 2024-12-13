import pandas as pd

# File and thresholds
excel_file = "/Users/ashnikapadia/Downloads/BGM data.xlsx"
df = pd.read_excel(excel_file)
critical_low = 54
critical_high = 250

# Read the Excel file
df = pd.read_excel(excel_file)

patients = df[['PtID', 'GlucoseValue']]

# Identify critical patients
critical_patients = patients[(patients['GlucoseValue'] < critical_low) | (patients['GlucoseValue'] > critical_high)]

# Print critical patients
if critical_patients.empty:
    print("No patients currently meet the critical criteria.")
else:
    print("Patients with critical glucose levels:")
    print(critical_patients)
