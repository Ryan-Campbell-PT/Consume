import json
from nutritionixApiWork import getNutritionInfo
from nutritionixApiDataManipulation import manipulate

def main():
    # get from text (json) file, containing date and food associated 
    naturalLanguageString = "3 large eggs, 2 baked chicken thighs, 1 head of broccoli"    
    dailyNutritionInfo = json.load(open('DailyNutrition.json'))
    
    jsonObj = json.load(open('output.json'))
    manipulate(jsonObj)

    for day in dailyNutritionInfo['Daily Nutrition Info']:
        date = day['Date']
        food = day['Food']

        nutInfo = getNutritionInfo(food)
        # write to db using date, string, and all nutrition info

    # nutInfo = getNutritionInfo(naturalLanguageString)
    # with open('output.json', 'a') as f:
    #     print(json.dumps(nutInfo, indent=4), file=f)
    #     f.close()
    

main()
