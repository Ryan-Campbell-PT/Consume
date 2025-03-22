import sqlite3
from NutritionRecordClass import DailyNutritionRecord

def executeDbCommand(dbCommand: str) -> bool:
    with sqlite3.connect("foodDb.db") as conn:
        cursor = conn.cursor()
        cursor.execute(dbCommand)
        conn.commit()

        return True
    return False

def createTable():
    tableStr = """  CREATE TABLE IF NOT EXISTS Daily(
                        Date VARCHAR(32),
                        FoodEaten VARCHAR(512),
                        Calories INTEGER,
                        Total Fat INTEGER,
                        Saturated Fat INTEGER,
                        Cholesterol INTEGER,
                        Sodium INTEGER,
                        Carbs INTEGER,
                        Fiber INTEGER,
                        Sugar INTEGER,
                        Protein INTEGER
                   )"""
    
    executeDbCommand(tableStr)

createTable()

def writeDailyNutrition(dailyNutritionRecord: DailyNutritionRecord):
    insertStr = f"""
        INSERT INTO Daily (Date, FoodEaten, Calories, TotalFat, SaturatedFat, Cholesterol, Sodium, Carbs, Fiber, Sugar, Protein)
        VALUES (
        '{dailyNutritionRecord.date}',
        '{dailyNutritionRecord.totalFoodString}',
        {dailyNutritionRecord.totalNutritionInfo.calories},
        {dailyNutritionRecord.totalNutritionInfo.totalFat},
        {dailyNutritionRecord.totalNutritionInfo.saturatedFat},
        {dailyNutritionRecord.totalNutritionInfo.cholesterol},
        {dailyNutritionRecord.totalNutritionInfo.sodium},
        {dailyNutritionRecord.totalNutritionInfo.carbs},
        {dailyNutritionRecord.totalNutritionInfo.fiber},
        {dailyNutritionRecord.totalNutritionInfo.sugar},
        {dailyNutritionRecord.totalNutritionInfo.protein}
        )
    """

    return executeDbCommand(insertStr)
