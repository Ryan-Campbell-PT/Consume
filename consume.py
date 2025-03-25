import json
from nutritionixApiWork import getNutritionInfo
from nutritionixApiWork import getDailyNutritionRecord
from databaseOperations import writeDailyNutrition
from visualization import visualize

def main():
    dailyNutritionJson = json.load(open('DailyNutrition.json'))
    
    # jsonObj = json.load(open('output.json'))
    # manipulate(jsonObj)

    for day in dailyNutritionJson['Daily Nutrition Info']:
        # first work daily info
        date = day['Date']
        foodString = day['Food']

        dailyRecord = getDailyNutritionRecord(date, foodString) 
        writeDailyNutrition(dailyRecord)
        
    for customRecipes in dailyNutritionJson['Custom Recipes']:
        break
    # nutInfo = getNutritionInfo(naturalLanguageString)
    # with open('output.json', 'a') as f:
    #     print(json.dumps(nutInfo, indent=4), file=f)
    #     f.close()
    
    visualize()

main()
