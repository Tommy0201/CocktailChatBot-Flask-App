from collections import Counter
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import csv

# Load and preprocess the cocktail data
def load_cocktail_data():
    df = pd.read_csv('recommend_sys/vectorized_cocktail_data_5.csv', sep=',', quoting=csv.QUOTE_NONNUMERIC, converters={'vector': literal_eval})
    df['vector'] = df['vector'].apply(np.array)
    return df

# Preprocess the ingredients, characteristics, and weight lists
ingredients = ['whiskey','gin','rum','tequila','vodka','brandy',"champagne","wine","absinthe","coffee","egg white"]
characteristics = ['sweet', 'sour','bitter','spicy','salty','citrusy','floral','herbal','creamy','vanilla','caramel','fruity','coffee','smoky','nutty','carbonated']
weight = ['heavy','light']

# Load the cocktail data outside the function
cocktail_df = load_cocktail_data()

def recommend_cocktails(input_string, layer, type):
    user_ingredients = ""
    user_taste = ""
    user_weight = ""
    default_ans = """Please press:
                   0 for cocktail recommendations
                   1 for ingredients in a specific cocktail
                   2 for taste of a specific cocktail
                   3 for heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                   4 for history of a specific cocktail"""

    def validate_input(user_input, valid_values):
        user_tokens = [token.strip() for token in user_input.split(',')]
        if all(token in valid_values for token in user_tokens):
            return user_tokens
        else:
            return "invalid"

    def counter_to_vector(counter, user_weight):
        vector = [counter.get(item, 0) * 5 if item in ingredients else counter.get(item, 0) for item in ingredients + characteristics]
        if user_weight[0] == "heavy":
            vector.append(3)
        else:
            vector.append(0)
        return np.array(vector)

    if layer == 0 and input_string == "0":
        type = "recommend"
        layer += 1
        ingredients_string = ', '.join(ingredients)
        return f"""
Here are the ingredients: 
{ingredients_string}
What kind of ingredients would you like? """, layer, type

    elif layer == 1 and type == "recommend":
        user_ingredients = validate_input(input_string.lower(), ingredients)
        layer += 1
        if user_ingredients == "invalid":
            layer = 0
            type = ""
            return f"""Invalid input. Please restart.
                   {default_ans}""", layer, type
        characteristics_string = ', '.join(characteristics)
        return f"""
    Here are the taste: 
    {characteristics_string}
    Repeat more than once for more prevalent taste
    What kind of taste would you like? """, layer, type

    elif layer == 2 and type == "recommend":
        user_taste = validate_input(input_string.lower(), characteristics)
        layer += 1
        if user_taste == "invalid":
            layer = 0
            type = ""
            return f"""Invalid input. Please restart.
                   {default_ans}""", layer, type
        return """
Heavy or Light: """, layer, type

    elif layer == 3 and type == "recommend":
        layer = 0
        type = ""
        user_weight = validate_input(input_string.lower(), weight)
        if user_weight == "invalid":
            layer = 0
            return f"""Invalid input. Please restart.
                   {default_ans}""", layer, type
        user_tokens = user_ingredients + user_taste
        user_counter = Counter(user_tokens)
        user_vector = counter_to_vector(user_counter, user_weight)

        # Use the pre-loaded cocktail_df for recommendations
        cocktail_df['cosine_similarity'] = cocktail_df['vector'].apply(lambda x: cosine_similarity([user_vector], [x])[0][0])
        df_sorted = cocktail_df.sort_values(by='cosine_similarity', ascending=False)
        rec_cocktails = df_sorted.head(5)

        counter = 1
        ans = []
        for index, row in rec_cocktails.iterrows():
            counter += 1
            ans.append(f"""
                {counter-1}) Cocktail: {row['Cocktail Name']}
                Ingredients: {row['Ingredients']}
                Taste: {row['combined']}
                Weight: {row['Weight']}
                   """)

        ans = "\n".join(ans)
        return ans, layer, type

    elif type != "recommend":
        return "invalid", layer, type

    else:
        return "invalid", 0, ""
