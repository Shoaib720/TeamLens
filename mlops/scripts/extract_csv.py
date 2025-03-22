import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Load environment variables
SHEET_ID = os.getenv("SHEET_ID")  # Google Sheet ID
SHEET_NAMES = os.getenv("SHEET_NAMES", "Sheet1,Sheet2").split(",")  # Multiple sheets

# Authenticate using service account JSON file
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = Credentials.from_service_account_file("creds.json", scopes=SCOPES)

# Connect to Google Sheets
client = gspread.authorize(creds)
for sheet_name in SHEET_NAMES:
    try:
        # Open each sheet
        sheet = client.open_by_key(SHEET_ID).worksheet(sheet_name.strip())

        # Read all values
        rows = sheet.get_all_values()

        # Ensure there's data in the sheet
        if len(rows) < 2:
            print(f"Skipping {sheet_name}: Not enough data.")
            continue

        # Extract only the table part (starting from row 2)
        df = pd.DataFrame(rows[2:], columns=rows[1])  # Use row 2 (index 1) as headers

        # Remove any duplicate headers in the data rows
        df = df[df.columns[df.iloc[0] != df.columns[0]]]  # Remove duplicate headers if found

        # Save DataFrame to CSV
        csv_filename = f"artifacts/{sheet_name.strip().replace(' ', '_').lower()}.csv"
        df.to_csv(csv_filename, index=False)

        print(f"CSV file '{csv_filename}' has been generated successfully!")

    except Exception as e:
        print(f"Error processing sheet {sheet_name}: {str(e)}")