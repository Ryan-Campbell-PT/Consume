import json


def manipulate(jsonDictDump):
    for foods in jsonDictDump['foods']:
        print(f"""
                Food: {foods['food_name']}
                Calories: {foods['nf_calories']}
                Sodium: {foods['nf_sodium']}
                Sugar: {foods['nf_sugars']}
                Protein: {foods['nf_protein']}
              """)