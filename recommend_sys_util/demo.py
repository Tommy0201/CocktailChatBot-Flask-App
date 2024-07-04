import pandas as pd



ingredients = ['whiskey', 'gin', 'rum', 'tequila', 'vodka', 'brandy', "champagne", "wine", "absinthe", "coffee", "egg white"]
characteristics = ['sweet', 'sour', 'bitter', 'spicy', 'salty', 'citrusy', 'floral', 'herbal', 'creamy', 'fruity', 'coffee', 'smoky', 'nutty', 'carbonated']

new = ["bourbon", "jack daniel’s", "islay single malt", "scotch", "calvados", "genever", "cognac", "armagnac", "pisco"]

ingredients_list = ["gin", "tequila", "cognac", "armagnac", "pimm’s", "sweet vermouth",
                    "dry vermouth", "campari", "chartreuse", "cointreau", "triple sec", "orange liqueur", "orange",
                    "grenadine", "amer picon", "maraschino", "midori", "dubonnet", "drambuie",
                    "velvet falernum", "mint", "cream", "creme", "crème", "butter", "beer", "ginger",
                    "soda", "amaretto", "egg white", "coffee", "rum", "vodka", "tequila", "absinthe",
                    "egg white", "champagne", "wine", "cola", "cranberry", "apricot", "lime", "lemon",
                    "passionfruit", "pineapple", "apple", "tomato", "strawberry","peach", "grape", "bitter", "cinnamon", "sugar",
                    "syrup", "gomme", "honey",'salt',"tabasco","vanilla","pepper","lillet","grand marnier","benedictine","nutmeg","condensed milk","worcestershire sauce", "prosecco","aperol"]

combined = ingredients + characteristics + new + ingredients_list

new_set = set(combined)

df = pd.read_csv("robust_cocktail.csv")

df["Ingredients"] = df["Ingredients"].str.lower().apply(lambda x: [ingredient.strip() for ingredient in x.split(',')])
result =[]

for index, row in df.iterrows():
    for ingredient in row["Ingredients"]:
        found = 0
        for x in new_set:
            if x in ingredient:
                found = 1
                break
        if found == 0:
            result.append(ingredient)
result = [x for x in result if "water" not in x and "half" not in x]
print(result)
                



