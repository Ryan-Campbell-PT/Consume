import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets as pySheet

def authorizeAndReturnSheet():

    with open('client_secret2.json') as serviceAccount:
        info = json.load(serviceAccount)
    client = pySheet.authorize('client_secret2.json')
    return client.open_by_key('1LIq4yREjOp5CVUewezhyjfFONbiA57LmncKrpL7466I')

def getNutritionDataList():
    date = input('Enter Date: ')
    rowToModify = getRowToModifyFromDate(date)
    with open('gptReturn.txt' ,'r') as file:
        for line in file.readlines():
            if(line.find(':') >= 0):
                fact = line.split(':')
                #so ideally at this point you would have the nutritional information (calorie)
                #in the first index and the second index would be the value
                key = fact[0].strip()
                value = fact[1].strip()
                #so ideally now you have all the info you need, so now to put it in the spreadsheet
                
                if(len(key) > 0 and len(value) > 0):
                    modifySpreadsheetWithData(key, value, rowToModify)
                

def modifySpreadsheetWithData(key, value, row):
    datacellList = sheet.find(key)[0] #list comes in an array of an array[[]], we only need the content so just grab first index
    if not datacellList:
        return
    cell = datacellList[0] #gets the actual cell
    # rowToModify = getRowToModifyFromDate(date)
    wks.update_value((row, cell.col), value)
    
    # allColumns = wks.get_col(cell.col) #you now have all columns, you need to find the first ''
    # rowIndexOfFirstEmptyString = allColumns.index('') + 1 #python index starts at 0, pysheets starts at 1
    # wks.update_value((rowIndexOfFirstEmptyString, cell.col), value)

def getRowToModifyFromDate(date):
    dateColumnList = sheet.find('Date')[0]
    fun = dateColumnList[0]
    dateCol = wks.get_col(fun.col)
    return dateCol.index(date) + 1 # +1 cause start at 0
    
sheet = authorizeAndReturnSheet()
wks = sheet.sheet1
datasetOfFacts = getNutritionDataList()
