import json
import requests
from nutritionixApiDataManipulation import makeDailyNutritionRecord

nutritionixDomain = "https://trackapi.nutritionix.com"
nutritionixEndpointNaturalNutrients = "/v2/natural/nutrients"
nutritionInformationEndpoint = nutritionixDomain + nutritionixEndpointNaturalNutrients

def getHeaders():
    data = json.load(open('nutritionixAPI.json'))
    return data

def getDailyNutritionRecord(date, naturalLanguageString):
    nutritionResponseJson = makeNutritionixRequest(naturalLanguageString)
    return makeDailyNutritionRecord(date, naturalLanguageString, nutritionResponseJson)

def getNutritionInfo(naturalLanguageString):
    nutritionResponseJson = makeNutritionixRequest(naturalLanguageString)
    #print(nutritionResponseJson)
    #return json.loads(f'{nutritionResponseJson}')
    return nutritionResponseJson

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
    
    except:
        return request.response()
    return