from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.thecocktailservice.co.uk/the-worlds-top-100-cocktails/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

def contains_recipe_or_ml(tag):
    return 'Recipe' in tag.text or any('{:d}ml'.format(i) in tag.text for i in range(10))

# Find all elements containing "Recipe" or "{integer}ml"
elements = soup.find_all(["h3", "p"])
filtered_elements = [element for element in elements if contains_recipe_or_ml(element)]

recipe_dict={}
# Print or use the elements as needed
for element in filtered_elements:
    if element.name=="h3":
        cocktail = element.text.replace("Recipe","").replace("Cocktail","").strip()
        recipe_dict[cocktail] = []
    elif element.name == "p" and cocktail:
        add = element.text.strip().split('\n')
        add = [x for x in add if "Garnish" not in x]
        recipe_dict[cocktail].append(add)


# File path to save the CSV
csv_file_path = 'robust_cocktail.csv'

# Write the dictionary to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Cocktail Name', 'Ingredients']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write each entry
    for cocktail, ingredients_list in recipe_dict.items():
        writer.writerow({'Cocktail Name': cocktail, 'Ingredients': ','.join(ingredients_list[0])})