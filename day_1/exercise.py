# ITP Week 4 Day 1 Exercise

# https://data.messari.io/api/v2/assets

import requests
import json
import openpyxl

#wb = openpyxl.load_workbook("C:/Users/jessy/Desktop/Vetstech_Python/itp_week_4/day_1/output.xlsx")
#sheet = wb['sheet1']

def get_data(url):
    response = requests.get(url)
    json_result = response.text
    #print(response)
    clean_data = json.loads(json_result)
    result = clean_data["data"]
    return result

#row = 1 

data = get_data ("https://data.messari.io/api/v2/assets")
symbols = [] 
print(data) # data comes out

#for i in data:

# def write_data(result):
#       global row
#       for character in result:
#          symbols.append(character['symbol'])

# print(symbols)



#         sheet['A' + str(row)] = character['id']
#         sheet['B' + str(row)] = character['symbol']
#         sheet['C' + str(row)] = character['name']
#         sheet['D' + str(row)] = character['slug']
#         row+=1
