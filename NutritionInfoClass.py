# This class represents the individual records for the food returned by the api
class NutritionInfo:
    # servingSize: int
    # calories: int
    # fat: int
    # cholesterol: int
    # sodium: int
    # carbs: int
    # fiber: int
    # sugar: int
    # protein: int

    def addAndReturn(self, nutritionInfoObj):
        ret = NutritionInfo(
            self.calories + nutritionInfoObj.calories,
            self.fat + nutritionInfoObj.fat,
            self.cholesterol + nutritionInfoObj.cholesterol,
            self.sodium + nutritionInfoObj.sodium,
            self.carbs + nutritionInfoObj.carbs,
            self.fiber + nutritionInfoObj.fiber,
            self.sugar + nutritionInfoObj.sugar,
            self.protein + nutritionInfoObj.protein
        )
        return ret

    def addToSelf(self, nutritionInfoObj):
        self.calories += nutritionInfoObj.calories
        self.fat += nutritionInfoObj.fat
        self.cholesterol += nutritionInfoObj.cholesterol
        self.sodium += nutritionInfoObj.sodium
        self.carbs += nutritionInfoObj.carbs
        self.fiber += nutritionInfoObj.fiber
        self.sugar += nutritionInfoObj.sugar
        self.protein += nutritionInfoObj.protein
        #return self
    
    def __init__(self,
                 servingSize=0,
                 calories=0,
                 fat=0,
                 cholesterol=0,
                 sodium=0,
                 carbs=0,
                 fiber=0,
                 sugar=0,
                 protein=0
                 ):
        self.servingSize = round(servingSize)
        self.calories = round(calories)
        self.fat = round(fat)
        self.cholesterol = round(cholesterol)
        self.sodium = round(sodium)
        self.carbs = round(carbs)
        self.fiber = round(fiber)
        self.sugar = round(sugar)
        self.protein = round(protein)

    def __str__(self):
        return (
            f"""
                Serving Size: {self.servingSize}
                Calories: {self.calories}
                Fat: {self.fat}
                Cholesterol: {self.cholesterol}
                Sodium: {self.sodium}
                Carbs: {self.carbs}
                Fiber: {self.fiber}
                Sugar: {self.sugar}
                Protein: {self.protein}
              """
        )