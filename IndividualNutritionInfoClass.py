# This class represents the individual records for the food returned by the api
class IndividualNutritionInfo:
    # foodName: str
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
        ret = IndividualNutritionInfo(
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
                 foodName='',
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
        self.foodName = foodName
        self.servingSize = servingSize
        self.calories = calories
        self.fat = fat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.carbs = carbs
        self.fiber = fiber
        self.sugar = sugar
        self.protein = protein

    def __str__(self):
        return (
            f"""
                Food: {self.foodName}
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