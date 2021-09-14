# ITP Week 4 Day 1 Lecture
# https://rickandmortyapi.com/api/character

## GET THE DATE
## CLEAN THE DATA
## LOOP THROUGH DATA
## OUTPUT THE DATA
# ITP Week 4 Day 1 Lecture

import requests
import json
import openpyxl

wb = openpyxl.load_workbook("/Users/jessy/Desktop/Vetstech_Python/itp_week_4/day_1/output.xlsx")
sheet = wb["Sheet1"]

def get_data(url):
    response = requests.get(url)
    # print(response)
    json_result = response.text
    # print(json_result)
    # print(type(json_result))
    clean_data = json.loads(json_result)
    result = clean_data["results"]
    return result

row = 1

def write_data(result):
    global row
    for character in result:
        sheet['A' + str(row)] = character['name']
        sheet['B' + str(row)] = character['species']
        sheet['C' + str(row)] = character['gender']
        sheet['D' + str(row)] = character['location']['name']
        row+=1


result_1 = get_data("https://rickandmortyapi.com/api/character")
result_2 = get_data("https://rickandmortyapi.com/api/character/?page=2")
result_3 = get_data("https://rickandmortyapi.com/api/character/?page=3")

write_data(result_1)
write_data(result_2)
write_data(result_3)
write_data(get_data("https://rickandmortyapi.com/api/character/?page=4"))


wb.save("/Users/jessy/Desktop/Vetstech_Python/itp_week_4/day_1/output.xlsx")