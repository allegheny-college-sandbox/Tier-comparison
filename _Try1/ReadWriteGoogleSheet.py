# Imports needed
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd()+'/secret_key/key.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("Tier-comparison")
sheet = workbook.sheet1
grades = 'C2:C5'

# Separate the grades in tiers by comparing with numbers
for cell in sheet.range(grades):
    if 100 > 90:
        print("green")
        print(cell.value)
        print("-----------------")
    elif 30 < 60:
        print("red")
        print(cell.value)
        print("-----------------")
    elif 90 > 80 > 70:
        print("yellow")
        print(cell.value)
        print("-----------------")
    else:
        pass