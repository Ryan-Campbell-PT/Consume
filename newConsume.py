import json
from nutritionixApiWork import getNutritionInfo
from nutritionixApiWork import getDailyNutritionRecord
from databaseOperations import writeDailyNutrition

def main():
    dailyNutritionJson = json.load(open('DailyNutrition.json'))
    
    # jsonObj = json.load(open('output.json'))
    # manipulate(jsonObj)

    for day in dailyNutritionJson['Daily Nutrition Info']:
        date = day['Date']
        foodString = day['Food']

        dailyRecord = getDailyNutritionRecord(date, foodString) 
        print("DB Success: " + str(writeDailyNutrition(dailyRecord)))
        
        # write to db using date, string, and all nutrition info

    for customRecipes in dailyNutritionJson['Custom Recipes']:
        break
    # nutInfo = getNutritionInfo(naturalLanguageString)
    # with open('output.json', 'a') as f:
    #     print(json.dumps(nutInfo, indent=4), file=f)
    #     f.close()
    

main()
