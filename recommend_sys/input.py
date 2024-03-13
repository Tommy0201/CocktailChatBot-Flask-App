from collections import Counter
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
from numpy.linalg import norm
import csv
import sys



def recommend_cocktails():
    ingredients = ['whiskey','gin','rum','tequila','vodka','brandy',"champagne","wine","absinthe","coffee","egg white"]
    characteristics = ['sweet', 'sour','bitter','spicy','salty','citrusy','floral','herbal','creamy','vanilla','caramel','fruity','coffee','smoky','nutty','carbonated']
    weight = ['heavy','light']
    nums_list = [str(i) for i in range(1,11)]

    def validate_input(user_input, valid_values):
        user_tokens = [token.strip() for token in user_input.split(',')]
        if all(token in valid_values for token in user_tokens):
            return user_tokens
        else:
            print("Invalid input. Please re-enter.")
            return validate_input(input("Try again: "), valid_values)
    def validate_number(user_input,nums_list):
        if user_input in nums_list:
            return user_input
        else:
            print("Invalid input. Please re-enter.")
            return validate_number(input("Try again: "),nums_list)
    def counter_to_vector(counter,user_weight):
        vector = [counter.get(item, 0) * 5 if item in ingredients else counter.get(item, 0) for item in ingredients + characteristics]
        if user_weight[0] == "heavy":
            vector.append(3)
        else:
            vector.append(0)
        return np.array(vector)


    while True:
        val1 = input(f"""
Here are the ingredients: {ingredients}
What kind of ingredients would you like? """)

        user_ingredients =  validate_input(val1.lower(), ingredients)
            
        val2 = input(f"""
Here are the taste: {characteristics}
Repeat more than once for more prevalent taste
What kind of taste would you like? """)
        user_taste =  validate_input(val2.lower(), characteristics)
        val3 = input("""
Heavy or Light: """)
        user_weight = validate_input(val3.lower(),weight)    
        val4 = input ("""
Numer of suggestions (max 10): """)
        user_number = validate_number(val4.lower(),nums_list)
        user_number = int(user_number)
        user_tokens = user_ingredients+user_taste
        user_counter = Counter(user_tokens)
        user_vector = counter_to_vector(user_counter,user_weight)
        # print(f"user vector: {user_vector}")
        # print(len(user_vector))

        df = pd.read_csv('recommend_sys/vectorized_cocktail_data_4.csv', sep=',', quoting=csv.QUOTE_NONNUMERIC, converters={'vector': literal_eval})

        df['vector'] = df['vector'].apply(np.array)

        df['cosine_similarity'] = df['vector'].apply(lambda x: cosine_similarity([user_vector], [x])[0][0])
        df_sorted = df.sort_values(by='cosine_similarity', ascending=False)
        rec_cocktails = df_sorted.head(user_number)
        # print(df_sorted)
        counter = 1
        for index, row in rec_cocktails.iterrows():
            print(f"{counter}) Cocktail: {row['Cocktail Name']}")
            print(f"   Ingredients: {row['Ingredients']}")
            print(f"   Taste: {row['combined']}")
            print(f"   Weight: {row['Weight']}")
            print("\n")
            counter +=1
        continue_input = input("Bot: Would you want another recommendation? (yes/no): ").lower()
        if continue_input!='yes':
            break

