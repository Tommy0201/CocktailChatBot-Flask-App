from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.liquor.com/classic-cocktails-5217936"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")

elements = soup.find_all("a")
count = 1
list_url = []
for link in elements:
    if link["href"].startswith("https://www.liquor.com/recipes/"):
        if "Get the recipe." in link:
            list_url.append(link["href"])

new_dict = {}
patterns = ["ounces","dashes","ounce","dash","teaspoon"]
for drink in list_url:
    p = requests.get(drink)
    soup2 = BeautifulSoup(p.content,"html.parser")
    drink_name = soup2.find("h1",class_="heading__title").get_text(strip=True)
    ingredients = []
    elements2 = soup2.find_all("li",class_="structured-ingredients__list-item")
    for e in elements2:
        ingredient = e.get_text(strip=True)
        if "garnish" not in ingredient.lower() and "water" not in ingredient.lower():
            for pat in patterns:
                match = re.search(f'{pat}\s*(.*)', ingredient)
                if match:
                    ingredient = match.group(1).strip()
                    if "weet" in ingredient or "imple" in ingredient:
                        ingredient = "s" + ingredient
                    break
            ingredients.append(ingredient)
        new_dict[drink_name] = ingredients

csv_file_path = "cocktail_data.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Cocktail Name', 'Ingredients'])
    
    for cocktail_name, ingredients in new_dict.items():
        writer.writerow([cocktail_name, ', '.join(ingredients)])

print(f'The data has been saved to {csv_file_path}')