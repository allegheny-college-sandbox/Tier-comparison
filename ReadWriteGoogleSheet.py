# Imports needed
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv(GOOGLE_SHEET_KEY), scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("Test_grades")
sheet = workbook.sheet1
grades = 'C2:C5'

# Separate the grades in tiers by comparing with numbers

# worksheet = some_spreadsheet.worksheet("Tier-comparison")

# colors:
# green = cellFormat(backgroundColor=color(0, 1, 0))
# yellow = cellFormat(backgroundColor=color(1, 1, 0))
# red = cellFormat(backgroundColor=color(1, 0, 0))

# What type of data is this? sheet.range(grades), it's probably an iterable.
# What type of data is cell?
# If it's an object, what do you need to call to get the value

# sheet.format(f"C{cell.row}",{"textFormat": {"foregroundColor": {"red": 0.0,"green": 1.0,"blue": 0.0}}})

def greentier():
    for cell in sheet.range(grades):
        if 100 > int(cell.value) and int(cell.value) > 90:
            print("-----------------")
            print("green")
            print(cell.value)
            print((sheet.cell(cell.row,cell.col+1)).value)
            sheet.format(f"C{cell.row}",{"backgroundColor": {"red": 0.0,"green": 1.0,"blue": 0.0}})
            print("-----------------")
        else:
            pass

def yellowtier():
    for cell in sheet.range(grades):
        if 90 > int(cell.value) and int(cell.value) > 70:
            print("yellow")
            print(cell.value)
            print((sheet.cell(cell.row,cell.col+1)).value)
            sheet.format(f"C{cell.row}",{"backgroundColor": {"red": 1.0,"green": 1.0,"blue": 0.0}})
            print("-----------------")
        else:
            pass

def redtier():
    for cell in sheet.range(grades):
        if 60 > int(cell.value) and int(cell.value) > 0:
            print("red")
            print(cell.value)
            print((sheet.cell(cell.row,cell.col+1)).value)
            sheet.format(f"C{cell.row}",{"backgroundColor": {"red": 1.0,"green": 0.0,"blue": 0.0}})
            print("-----------------")
        else:
            pass


if __name__ == "__main__":
    greentier()
    yellowtier()
    redtier()
