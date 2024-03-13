import csv 
import json

with open('recommend_sys/robust_cocktail_3.csv','r', newline='',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    df = {row['Cocktail Name']:row for row in reader}



formatted_df = {}
for names, data in df.items():
    formatted_df[names] = {
        "Ingredients": [x.strip() for x in data['Ingredients'].split(',')],
        "Taste": eval(data['Taste']),
        "Alcohol": eval(data['Ingredient_Break_Down']),
        "Weight": data["Weight"],
        "History": ""
    }
with open("formatted_cocktails1.json",'w',encoding='utf-8') as jsonfile:
    json.dump(formatted_df,jsonfile,indent = 4)
print("Completed")