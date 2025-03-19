import json
from nutritionixApiWork import getNutritionInfo
from nutritionixApiWork import getDailyNutritionRecord

def main():
    dailyNutritionInfo = json.load(open('DailyNutrition.json'))
    
    # jsonObj = json.load(open('output.json'))
    # manipulate(jsonObj)

    for day in dailyNutritionInfo['Daily Nutrition Info']:
        date = day['Date']
        foodString = day['Food']

        dailyRecord = getDailyNutritionRecord(date, foodString )
        print(dailyRecord)
        # nutInfo = getNutritionInfo(food)
        # write to db using date, string, and all nutrition info

    # nutInfo = getNutritionInfo(naturalLanguageString)
    # with open('output.json', 'a') as f:
    #     print(json.dumps(nutInfo, indent=4), file=f)
    #     f.close()
    

main()
