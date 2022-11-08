import gspread
from ouath2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(TODO: Absolute path, scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("Tier-comparison")
sheet = workbook.sheet1

