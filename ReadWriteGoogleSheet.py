# Imports needed
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *

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

# colors:
green = cellFormat(backgroundColor=color(0, 255, 0))
yellow = cellFormat(backgroundColor=color(255, 255, 0))
red = cellFormat(backgroundColor=color(255, 0, 0))

# What type of data is this? sheet.range(grades), it's probably an iterable.
# What type of data is cell?
# If it's an object, what do you need to call toget the value
for cell in sheet.range(grades):
    if 100 > int(cell.value) and int(cell.value) > 90:
        print("green")
        (workbook,[(cell, green)])
        print(cell.value)
        print("-----------------")
    elif 60 > int(cell.value) and int(cell.value) > 0:
        print("red")
        (workbook,[(cell, red)])
        print(cell.value)
        print("-----------------")
    elif 90 > int(cell.value) and int(cell.value) > 70:
        print("yellow")
        (workbook,[(cell, yellow)])
        print(cell.value)
        print("-----------------")
    else:
        pass