import sqlite3


def executeDbCommand(dbCommand):
    with sqlite3.connect("foodDb.db") as conn:
        cursor = conn.cursor()

        cursor.execute(dbCommand)

        conn.commit()
    

def createTable():
    tableStr = """  CREATE TABLE IF NOT EXISTS Daily(
                        Date VARCHAR(32),
                        FoodEaten VARCHAR(512),
                        Calories INTEGER,
                        Fat: INTEGER,
                        Cholesterol: INTEGER,
                        Sodium: INTEGER,
                        Carbs: INTEGER,
                        Fiber: INTEGER,
                        Sugar: INTEGER,
                        Protein: INTEGER
                   )"""
    
    executeDbCommand(tableStr)
    
def insertIntoFoodTable(dailyNutritionRecord):
    insertStr = f"""
        INSERT INTO Daily (Date, FoodEaten, Calories, Fat, Cholesterol, Sodium, Carbs, Fiber, Sugar, Protein)
        VALUES (
        {dailyNutritionRecord.date},
        {dailyNutritionRecord.totalFoodString},
        {dailyNutritionRecord.totalNutritionInfo.calories},
        {dailyNutritionRecord.totalNutritionInfo.fat},
        {dailyNutritionRecord.totalNutritionInfo.cholesterol},
        {dailyNutritionRecord.totalNutritionInfo.sodium},
        {dailyNutritionRecord.totalNutritionInfo.carbs},
        {dailyNutritionRecord.totalNutritionInfo.fiber},
        {dailyNutritionRecord.totalNutritionInfo.sugar},
        {dailyNutritionRecord.totalNutritionInfo.protein}
        )
    """

    executeDbCommand(insertStr)
