import sqlite3
from NutritionRecordClass import DailyNutritionRecord

def executeDbCommand(dbCommand: str) -> bool:
    with sqlite3.connect("foodDb.db") as conn:
        cursor = conn.cursor()
        cursor.execute(dbCommand)
        conn.commit()

        return True
    return False

def executeSelectCommand(dbCommand: str):
    with sqlite3.connect("foodDb.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(dbCommand)
        return cursor.fetchall()
    
def createTables():
    from NutritionInfoClass import NutritionInfo
    # nutritionInfoStr = """
    #     Calories INTEGER,
    #     Total Fat INTEGER,
    #     Saturated Fat INTEGER,
    #     Cholesterol INTEGER,
    #     Sodium INTEGER,
    #     Carbs INTEGER,
    #     Fiber INTEGER,
    #     Sugar INTEGER,
    #     Protein INTEGER
    # """

    nutritionInfoStr = NutritionInfo.getNutritionInfoColumns()

    dailyTableStr = f"""
        CREATE TABLE IF NOT EXISTS Daily(
            Date VARCHAR(32),
            FoodEaten VARCHAR(512),
            {nutritionInfoStr}
        )"""
    
    customObjsTableStr = f"""
        CREATE TABLE IF NOT EXISTS CustomRecipes(
            Name VARCHAR(50),
            Alternate Names VARCHAR(512),
            Serving Size INTEGER,
            {nutritionInfoStr}
        )"""
    
    executeDbCommand(dailyTableStr)
    executeDbCommand(customObjsTableStr)

createTables()

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

def getDailyRecord(date: str) -> DailyNutritionRecord:
    selectStr = f"""
        SELECT * FROM Daily WHERE Date = '{date}'
    """

    selectData = executeSelectCommand(selectStr)
    # for item in selectData:
    d = selectData[0]
    return DailyNutritionRecord(d)


    # calories: int
    # totalFat: int
    # saturatedFat: int
    # cholesterol: int
    # sodium: int
    # carbs: int
    # fiber: int
    # sugar: int
    # protein: int
