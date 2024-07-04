from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
import csv
import json

url = "https://blog.cheapism.com/popular-cocktails/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


elements = soup.find_all(["h2", "div"],class_=["h3 slide-title","rich-text"])

count = 1
cocktails = []
descriptions = []

for element in elements:
    if element.name == "h2":
        # print(f"{count}\n{element.text}")
        cocktails.append(element.text)
        count +=1
    if "rich-text" in element.get("class", []):
        first_p = element.find("p")
        if first_p:
            descriptions.append(first_p.text)

# count = 1
# for key, value in new_dict.items():
#     print(count)
#     print(f"Key: {key}\nValue: {value}")
#     count +=1

def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)

cocktail_data = load_json("formatted_cocktails1.json")
cocktail_names = list(cocktail_data.keys())
print(f"Cocktail Names JSON:\n{cocktail_names}")
print(f"cocktails:\n{cocktails[1:]}")
for i in range(len(cocktails)): 
    if cocktails[i] == "Pimm’s Cup":
        cocktails[i] = "Pimm's Cup"
    elif cocktails[i] == "Piña Colada":
        cocktails[i] = "Pina Colada"
updated_cocktails = []
updated_description = []
for i in range(len(cocktails)):
    if cocktails[i] in cocktail_names:
        updated_cocktails.append(cocktails[i])
        updated_description.append(descriptions[i])
for i in range(len(updated_cocktails)):
    print(updated_cocktails[i])
    print(updated_description[i])

new_dict={}
for i in range(1,len(updated_cocktails)):
    new_dict[updated_cocktails[i]] =updated_description[i]


# count = 1
# for key, value in new_dict.items():
#     print(count)
#     print(f"Key: {key}\nValue: {value}")
#     count +=1


for drink, history in new_dict.items():
    cocktail_data[drink]["History"] = history
with open("formatted_cocktail1.json",'w') as json_file:
    json.dump(cocktail_data,json_file,indent=2)