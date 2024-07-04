import pandas as pd

df = pd.read_csv("recommend_sys_util/robust_cocktail.csv")

def add_taste_ingre(row):
    tastes = []
    ingres=[]
    row["Ingredients"] = row["Ingredients"].lower()
    light_count = 0
    heavy_count = 0
    weight = "heavy"

    if "whiskey" in row["Ingredients"] or "bourbon" in row["Ingredients"] or "jack daniel’s" in row["Ingredients"] or "islay single malt" in row["Ingredients"] or "scotch" in row["Ingredients"] or "calvados" in row["Ingredients"]:
        tastes.extend(["spicy", "smoky",'vanilla','caramel'])
        ingres.append("whiskey")
        heavy_count+=1
    if "rum" in row["Ingredients"]:
        tastes.extend(["sweet"])
        heavy_count+=1
        if "light rum" in row["Ingredients"]:
            tastes.extend(['fruity'])
        if "dark rum" in row["Ingredients"]:
            tastes.extend(["caramel","smoky"])

    if "gin," in row["Ingredients"] or "genever" in row["Ingredients"]:
        tastes.extend(["floral", "herbal","spicy"])
        ingres.append("gin")
        heavy_count+=1

    if "tequila" in row["Ingredients"]:
        tastes.extend(["herbal","spicy"])
        heavy_count+=1

    if "cognac" in row["Ingredients"] or "armagnac" in row["Ingredients"] or "pisco" in row["Ingredients"] or "grand marnier" in row["Ingredients"]:
        tastes.extend(["fruity","sweet","spicy","caramel","vanilla"])
        ingres.extend(['brandy'])
        heavy_count+=1

    if "pimm’s" in row["Ingredients"]:
        tastes.extend(["citrusy", "sweet", "herbal"])
        heavy_count+=1

    if "sweet vermouth" in row["Ingredients"]:
        tastes.extend(["sweet", "spicy", 'herbal', "bitter"])
        heavy_count+=1
    if "dry vermouth" in row["Ingredients"]:
        tastes.extend(["floral", "herbal"])
        heavy_count+=1
    if "campari" in row["Ingredients"]:
        tastes.extend(["bitter", "citrusy"])
        heavy_count+=1
    if "grand marnier" in row["Ingredients"]:
        tastes.extend(["citrusy","bitter"])
        heavy_count+=1
    if "chartreuse" in row["Ingredients"]:
        tastes.extend(["floral", 'herbal', "spicy"])
        heavy_count+=1
    if "cointreau" in row["Ingredients"] or "triple sec" in row["Ingredients"] or "orange liqueur" in row["Ingredients"]:
        tastes.extend(["citrusy", "sweet"])
        heavy_count+=1
    if "orange juice" in row["Ingredients"]:
        tastes.extend(["citrusy","sweet"])
        light_count +=1
    if "grenadine" in row["Ingredients"]:
        tastes.extend(["fruity", "sweet"])
        heavy_count+=1
    if "amer picon" in row["Ingredients"]:
        tastes.extend(["bitter", "citrusy","herbal"])
        heavy_count+=1
    if "maraschino" in row["Ingredients"]:
        tastes.extend(["bitter","fruity","sour"])
        heavy_count+=1
    if "midori" in row["Ingredients"]:
        tastes.extend(["sweet","fruity"]) 
        heavy_count+=1
    if "dubonnet" in row["Ingredients"]:
        tastes.extend(["sweet","herbal","spicy"]) 
        heavy_count+=1
    if "drambuie" in row["Ingredients"]:
        tastes.extend(["sweet","spicy","herbal","smoky","caramel","vanilla"]) 
        heavy_count+=1
    if "velvet falernum" in row["Ingredients"]:
        tastes.extend(["sweet","spicy","citrusy"]) 
        heavy_count+=1
    if "benedictine" in row["Ingredients"]:
        tastes.extend(["floral","herbal","citrusy","sweet","spicy"])
        heavy_count+=1
    if "lillet" in row["Ingredients"]:
        tastes.extend(["sweet","fruity","citrusy","floral"])
        ingres.append("wine") 
    if "aperol" in row["Ingredients"]:
        tastes.extend(["sweet","herbal","citrusy","bitter"])
        heavy_count+=1
    if "prosecco" in row["Ingredients"]:
        tastes.extend(["fruity","floral", "citrusy", "carbonated"])
        ingres.append("wine")
    if "cachaça" in row["Ingredients"]:
        tastes.extend(["sweet","herbal","fruity"])
        heavy_count+=1
    if "cassis" in row["Ingredients"]:
        tastes.extend(["sweet","fruity"])
        heavy_count+=1
    if "mint" in row["Ingredients"]:
        tastes.append("herbal")
    if "elderflower" in row["Ingredients"]:
        tastes.extend(["floral","sweet"])
        heavy_count+=1
    if "cream" in row["Ingredients"] or "creme" in row["Ingredients"] or "crème" in row["Ingredients"] or "milk" in row["Ingredients"]:
        tastes.append("creamy")
        light_count +=1
    if "butter" in row["Ingredients"]:
        tastes.append("creamy")
    if "beer" in row["Ingredients"]:
        tastes.extend(["carbonated"])
        light_count +=1
    if "ginger" in row["Ingredients"]:
        tastes.extend(["spicy"])
    if "soda" in row["Ingredients"]:
        tastes.append("carbonated")
        light_count +=1
    if "amaretto" in row["Ingredients"]:
        tastes.extend(["sweet", "nutty"])
        heavy_count+=1
    if "egg white" in row["Ingredients"]:
        tastes.append("creamy")
        light_count +=1
    if "coffee" in row["Ingredients"]:
        tastes.append("caramel")
        heavy_count+=1
    if "condensed milk" in row["Ingredients"]:
        tastes.extend(["creamy","sweet"])
        light_count +=1
    
    if "coconut" in row["Ingredients"]:
        tastes.extend(["creamy","sweet"])
        light_count +=1
    listing = ["rum","vodka","tequila","absinthe","egg white","champagne","wine","coffee"]
    for x in listing:
        if x in row["Ingredients"]:
            ingres.append(x)
    if  "cranberry" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity","sour","bitter"])
        light_count+=1
    if "cola" in row["Ingredients"]:
        tastes.extend(["sweet","carbonated","caramel"])
        light_count+=1
    if "apricot" in row["Ingredients"]:
        tastes.extend(["herbal","floral"])
    if "lime" in row["Ingredients"] or "lemon" in row["Ingredients"] or "passionfruit" in row["Ingredients"]:
        tastes.extend(["citrusy", "sour"])
        light_count +=1
    if "passionfruit" in row["Ingredients"]:
        tastes.extend(["citrusy", "sour"])
        light_count +=1
    if "pineapple" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity"])
        light_count +=1
    if "apple" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity"])
        light_count +=1
    if "blackberry" in row["Ingredients"] or "cherry" in row["Ingredients"] or "chambord" in row["Ingredients"] or "raspberries" in row["Ingredients"] or "strawberry" in row["Ingredients"] or "fruit puree" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity"])
        light_count +=1   
    if "chambord" in row["Ingredients"]:
        tastes.append("vanilla") 
    if "violet" in row["Ingredients"]:
        tastes.extend(["sweet", "floral"])
        light_count +=1            
    if "peach" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity"])
        light_count +=1 
    if "grape" in row["Ingredients"]:
        tastes.extend(["sweet", "fruity"])
        light_count +=1     
    if "coconut" in row["Ingredients"]:
        tastes.extend(["sweet","creamy","nutty"])
        light_count +=1
    if "cinnamon" in row["Ingredients"]:
        tastes.append("spicy")
    if "pepper" in row["Ingredients"]:
        tastes.extend(["spicy","herbal"])
    if "tabasco" in row["Ingredients"]:
        tastes.extend(["spicy","spicy","sour"])
    if "vanilla" in row["Ingredients"]:
        tastes.append("vanilla")
    if "bitter" in row["Ingredients"]:
        tastes.append("bitter")
    if "syrup" in row["Ingredients"] or "gomme" in row["Ingredients"] or "honey" in row["Ingredients"] or "nutmeg" in row["Ingredients"]:
        tastes.append("sweet")
        light_count +=1
    if "sugar cube" in row["Ingredients"]:
        tastes.append("sweet")
    if "salt" in row["Ingredients"]:
        tastes.append("salty")


    if light_count >=1 and heavy_count <3:
        weight = "light"



    return pd.Series([tastes, ingres, weight ], index=['Taste', 'Ingredient_Break_Down','Weight'])

df[['Taste','Ingredient_Break_Down','Weight']] = df.apply(add_taste_ingre, axis=1)
df["Weight"] = df["Weight"].astype(str)

df.to_csv("recommend_sys_util/robust_cocktail_3.csv", index=False)