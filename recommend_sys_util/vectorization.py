from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
from ast import literal_eval
from collections import Counter
from numpy.linalg import norm
import csv


ingredients = ['whiskey','gin','rum','tequila','vodka','brandy',"champagne","wine","absinthe","coffee","egg white"]
characteristics = ['sweet', 'sour','bitter','spicy','salty','citrusy','floral','herbal','creamy','fruity','coffee','smoky','nutty','carbonated','caramel','vanilla']


df = pd.read_csv("recommend_sys_util/robust_cocktail_3.csv",converters={"Taste":literal_eval,"Ingredient_Break_Down":literal_eval})

df["combined"] = df.apply(lambda x: x["Ingredient_Break_Down"] + x["Taste"], axis=1)
df["combined"] = df["combined"].apply(lambda x: list(x))


# df["combined"] = [[] for _ in range(len(df))]

# for i in range(len(df["Taste"])):
#     df["combined"][i] = df["Ingredient_Break_Down"][i] + df["Taste"][i]


df["counter"] = [Counter(comb) for comb in df["combined"]]
def vectorize(dfr):
    vector = [0] * (len(ingredients + characteristics)+1)
    for item in dfr["Ingredient_Break_Down"]:
        if item in ingredients:
            vector[ingredients.index(item)] += 5
    for item in dfr["Taste"]:
        if item in characteristics:
            vector[len(ingredients) + characteristics.index(item)] += 1
    vector[-1] = 3 if dfr["Weight"].lower() == "heavy" else 0   
    return vector

df["vector"] = df.apply(vectorize, axis = 1)
print(type(df['combined'][1]))
df.to_csv('recommend_sys_util/vectorized_cocktail_data_5.csv', sep=',', quoting=csv.QUOTE_NONNUMERIC, index=False)

