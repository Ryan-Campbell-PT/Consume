class NutritionInfo:
    foodName: str
    servingSize: int
    calories: int
    fat: int
    cholesterol: int
    sodium: 0
    carbs: 0
    fiber: 0
    sugar: 0
    protein: 0

    def __init__(self,
                 servingSize,
                 calories,
                 fat,
                 cholesterol,
                 sodium,
                 carbs,
                 fiber,
                 sugar,
                 protein
                 ):
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