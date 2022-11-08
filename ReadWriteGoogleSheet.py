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

for cell in sheet.range('C2:C5'):
    if int(cell) > 90:
        print("green")
        print(int(cell).value)
        print("-----------------")
    elif int(cell) < 60:
        print("red")
        print(int(cell).value)
        print("-----------------")
    elif 90 > int(cell) > 70:
        print("yellow")
        print(int(cell).value)
        print("-----------------")
    else:
        pass