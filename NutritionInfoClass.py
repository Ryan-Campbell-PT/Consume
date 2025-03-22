# This class represents any nutrition info being stored
class NutritionInfo:
    # calories: int
    # totalFat: int
    # saturatedFat: int
    # cholesterol: int
    # sodium: int
    # carbs: int
    # fiber: int
    # sugar: int
    # protein: int

    def addAndReturn(self, nutritionInfoObj):
        ret = NutritionInfo(
            self.calories + nutritionInfoObj.calories,
            self.totalFat + nutritionInfoObj.totalFat,
            self.saturatedFat + nutritionInfoObj.saturatedFat,
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
        self.totalFat += nutritionInfoObj.totalFat
        self.saturatedFat += nutritionInfoObj.saturatedFat
        self.cholesterol += nutritionInfoObj.cholesterol
        self.sodium += nutritionInfoObj.sodium
        self.carbs += nutritionInfoObj.carbs
        self.fiber += nutritionInfoObj.fiber
        self.sugar += nutritionInfoObj.sugar
        self.protein += nutritionInfoObj.protein
    
    def __init__(self,
                 calories=0,
                 totalFat=0,
                 saturatedFat=0,
                 cholesterol=0,
                 sodium=0,
                 carbs=0,
                 fiber=0,
                 sugar=0,
                 protein=0
                 ):
        self.calories = round(calories)
        self.totalFat = round(totalFat)
        self.saturatedFat = round(saturatedFat)
        self.cholesterol = round(cholesterol)
        self.sodium = round(sodium)
        self.carbs = round(carbs)
        self.fiber = round(fiber)
        self.sugar = round(sugar)
        self.protein = round(protein)

    def __str__(self):
        return (
            f"""
                Calories: {self.calories}
                Total Fat: {self.totalFat}
                Saturated Fat: {self.saturatedFat}
                Cholesterol: {self.cholesterol}
                Sodium: {self.sodium}
                Carbs: {self.carbs}
                Fiber: {self.fiber}
                Sugar: {self.sugar}
                Protein: {self.protein}
              """
        )