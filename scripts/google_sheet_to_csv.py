import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Load environment variables
SHEET_ID = os.getenv("SHEET_ID")  # Google Sheet ID
SHEET_NAME = os.getenv("SHEET_NAME", "Sheet1")  # Default Sheet Name

# Authenticate using service account JSON file
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = Credentials.from_service_account_file("creds.json", scopes=SCOPES)

# Connect to Google Sheets
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

# Get all records and convert to DataFrame
data = sheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[1])

# Save DataFrame to CSV
csv_filename = "google_sheet.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' has been generated successfully!")
