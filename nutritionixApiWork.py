import json
import requests
from nutritionixApiDataManipulation import makeDailyNutritionRecord
from NutritionRecordClass import DailyNutritionRecord

with open('nutritionixAPI.json') as f:
    nutritionix_data = json.load(f)

nutritionInformationEndpoint = nutritionix_data["Domain"] + nutritionix_data["NaturalLanguageEndpoint"]

def getHeaders():
    return nutritionix_data["Headers"]

def getDailyNutritionRecord(date, naturalLanguageString) -> DailyNutritionRecord:
    nutritionResponseJson = makeNutritionixRequest(naturalLanguageString)
    return makeDailyNutritionRecord(date, naturalLanguageString, nutritionResponseJson)

def getNutritionInfo(naturalLanguageString):
    nutritionResponseJson = makeNutritionixRequest(naturalLanguageString)
    #print(nutritionResponseJson)
    #return json.loads(f'{nutritionResponseJson}')
    return nutritionResponseJson

def handleErrors(request):
    return

def makeNutritionixRequest(naturalLanguageString):
    #queryJson = {"query": f'{naturalLanguageString}'} #this may have to be toString()ed
    queryJson = {"query": naturalLanguageString}
    try:
        request = requests.post(nutritionInformationEndpoint,
                                 json=queryJson,
                                 headers=getHeaders()
                                )
        
        if(request.status_code == 200):
            return request.json()
        else:
            handleErrors(request)
    except:
        return request.response()
    return