import json
from NutritionInfoClass import IndividualNutritionInfo
from NutritionRecordClass import DailyNutritionRecord


def makeDailyNutritionRecord(date, foodString, nutritionResponseJson):
    ret = DailyNutritionRecord(date=date, foodString=foodString)
    for foods in nutritionResponseJson['foods']:
        nutInfo = IndividualNutritionInfo(
            foods['food_name'],
            foods['serving_qty'],
            foods['nf_calories'],
            foods['nf_total_fat'],
            foods['nf_cholesterol'],
            foods['nf_sodium'],
            foods['nf_total_carbohydrate'],
            foods['nf_dietary_fiber'],
            foods['nf_sugars'],
            foods['nf_protein']
        )
        ret.addToNutritionInfo(nutInfo)
    
    return ret
