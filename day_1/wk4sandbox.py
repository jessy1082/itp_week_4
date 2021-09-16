import requests
import json
import openpyxl

wb = openpyxl.load_workbook("/home/")


def get_data():
    response = requests.get(url)
    #print(response)
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
        sheet['D' + str(row)] = character['']
