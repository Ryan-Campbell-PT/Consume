import json
from NutritionInfoClass import NutritionInfo

def manipulate(jsonDictDump):
    for foods in jsonDictDump['foods']:
        nutInfo = NutritionInfo(
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
