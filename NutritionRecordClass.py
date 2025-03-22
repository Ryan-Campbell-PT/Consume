from NutritionInfoClass import NutritionInfo
import math

# This class represents the total nutrition info for the day
# representing all the expected info placed into the Daily.db
class DailyNutritionRecord:
    # date: str
    # totalFoodString: str
    # totalNutritionInfo: NutritionInfo

    def __init__(self, date, foodString):
        self.date = date
        self.totalFoodString = foodString
        self.totalNutritionInfo = NutritionInfo()

    def __str__(self):
        return (f"""Date: {self.date}
                    Food String: {self.totalFoodString}
                    {self.totalNutritionInfo}"""
                )
    
    def getTotalNutritionInfo(self):
        # ret = NutritionInfo
        # for info in self.nutritionInfo:
        #     ret.addToSelf(info)

        return self.totalNutritionInfo

    def addToNutritionInfo(self, nutritionInfo):
        # if not self.nutritionInfo:
        #     self.nutritionInfo = []
        # else:
        #     self.nutritionInfo.append(nutritionInfo)
        self.totalNutritionInfo.addToSelf(nutritionInfo)

class WeeklyNutritionRecord:
    def __init__(self):
        pass