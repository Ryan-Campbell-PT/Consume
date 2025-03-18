import json
from getNutritionInfo import getNutritionInfo

def main():
    naturalLanguageString = "" # get from commandline
    # will have to test the data,
    # but i think each individual food will need to be parsed
    # there may be a final value, dunno
    getNutritionInfo(naturalLanguageString)
