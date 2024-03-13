import json
import re
import default_responses
from recommend_sys.input import recommend_cocktails
import random
import pandas as pd
from ast import literal_eval

# Load JSON data
def load_json(file, encoding='utf-8'):
    with open(file, encoding='utf-8') as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)

response_data = load_json("bot.json")
cocktail_data = load_json("history_cocktails.json")
cocktail_names = list(cocktail_data.keys())

def get_response(input_string):
    split_message = re.findall(r'\b\w+\b', input_string.lower())
    score_list = []
    cocktailss = []
    cocktail_check = {name:len(name.split()) for index,name in enumerate(cocktail_names)}
    names_tracker = list(cocktail_data.keys())
    names_tracker = [x.lower() for x in names_tracker]

    # Detect the names of cocktail being asked
    for word in split_message:
        for drink in cocktail_names:  
            i = cocktail_names.index(drink)
            if word.lower() in names_tracker[i].split():
                cocktail_check[drink] -= 1
                names_tracker[i] = names_tracker[i].replace(word.lower(),"").strip()
    for key, value in cocktail_check.items():
        if value == 0:
            cocktailss.append(key)
    # print(cocktailss)
    important_words = ["do","abilities","capable","tasks","assist", "help","support","answer","ask",
                       "name","call","made", "called",
                       "ingredients","ingredient","recipe","taste","flavor","recommend","recommendations","recommendation","suggestion", "pick",
                       "heavy","light","heavier","lighter","heaviest","lightest","drunk","tispy","out","black","pass","heaviness","lightness","strong","strongest","stronger",
                       "when","history", "origin","origins","story","backstory","behind","invented","originate","stories","background","tales","tale"]

    #Calculate the score to match question type
    for response in response_data:
        response_score = 0
        for word in split_message:
            if word.lower() in response["user_input"]:
                response_score += 1
                if word.lower() in important_words:
                    response_score +=4
        score_list.append(response_score)

    best_response = max(score_list)
    best_index = score_list.index(best_response)
    # print(score_list)

    if input_string == "":
        return "Input invalid. Please type something"
    # If there is at least a match in words
    if best_response != 0:
        #Recommend cocktails
        n = len(response_data[best_index]["bot_response"])
        default_ans = response_data[best_index]["bot_response"][random.randrange(n)]
        if response_data[best_index]["response_type"] == "job":
            return(f"Bot: {default_ans}\n1) ingredients in a specific cocktail\n2) taste of a specific cocktail\n3) heaviness/lightness of a cocktail or comparing the weight among different given cocktails\n4) history of a specific cocktail\n5) cocktail recommendations.")
        elif response_data[best_index]["response_type"] == "recommendation":
            print(f"Bot: {default_ans}")
            return recommend_cocktails() 
        #Check ingredients in cocktails
        elif response_data[best_index]["response_type"] == "check":
            cocktail = cocktailss[0]
            if cocktail!="":
                ingredients = set()
                for word in split_message:
                    if word.lower() in response_data[best_index]["user_input"]:
                        ingredients.add(word)
                ingredients = list(ingredients)
                # print(f"Ingredients: {ingredients}")
                for x in ingredients:
                    found_match = False
                    found_submatch = False
                    if x in cocktail_data[cocktail]["Ingredients"]:
                        found_match = True
                    for y in cocktail_data[cocktail]["Ingredients"]:
                        if x.lower() in y.lower():
                            found_submatch = True
                            break
                    if not found_match and not found_submatch:
                        ans = response_data[best_index]["bot_response_neg"][random.randrange(len(response_data[best_index]["bot_response_neg"]))]
                        out = "Bot: " + ans
                        return out
                ans1 = response_data[best_index]["bot_response_pos"][random.randrange(len(response_data[best_index]["bot_response_pos"]))]
                out1 = "Bot: " + ans1
                return out1
         #Taste of cocktails   
        elif response_data[best_index]["response_type"] == "taste":
            if cocktailss:
                ans = ""
                print(f"Bot: {default_ans}")
                for cocktail in cocktailss:
                    if cocktail!="":
                        taste_output = set(cocktail_data[cocktail]["Taste"])
                        taste_output = ', '.join(list(taste_output))
                        ans += (f"{cocktail}\n{taste_output}\n")
                return ans
       #Ingredients of cocktails         
        elif response_data[best_index]["response_type"] == "ingredients":
            if cocktailss:
                ans = ""
                print(f"Bot: {default_ans}")
                for cocktail in cocktailss:
                    if cocktail!="":
                        out =', '.join(cocktail_data[cocktail]["Ingredients"])
                        ans += (f"{cocktail}\n{out}\n")
                return ans
        #The weight of cocktails
        elif response_data[best_index]["response_type"] == "heavy-or-light":
            if len(cocktailss) == 1:
                cocktail = cocktailss[0]
                if cocktail_data[cocktail]["Weight"].lower()== "heavy":
                    ans = response_data[best_index]["bot_response_pos"][random.randrange(len(response_data[best_index]["bot_response_pos"]))]
                    out = "Bot: " + ans
                    return out
                else: 
                    ans = response_data[best_index]["bot_response_neg"][random.randrange(len(response_data[best_index]["bot_response_neg"]))]
                    out = "Bot: " + ans
                    return out

            elif len(cocktailss) == 2:
                cocktail1, cocktail2 =  cocktailss[0], cocktailss[1]
                weight1, weight2 = cocktail_data[cocktail1]["Weight"].lower(),cocktail_data[cocktail2]["Weight"].lower()
                if weight1 == "heavy":
                    if weight2 == "heavy":
                        return "Bot: Both is heavy as far as I know."
                    else:
                        return (f"Bot: {cocktail1} is the heavier")
                else:
                    if weight2 == "heavy":
                        return (f"Bot: {cocktail2} is the heavier")
                    else:
                        return "Bot: Both is light according to my data"
            elif len(cocktailss) >=3: 
                heavy_lst = "Heavy: "
                light_lst = "Light: "
                for cocktail in cocktailss:
                    weight = cocktail_data[cocktail]["Weight"].lower()
                    if weight == 'heavy':
                        heavy_lst += f"{cocktail} "
                    else:
                        light_lst += f"{cocktail} "   
                return f"Bot: Here is what I can tell you based on my data:\n{heavy_lst}\n{light_lst}" 
            elif len(cocktailss) ==0:
                if "heaviest" in split_message or "lightest" in split_message:
                    return "Bot: I do not have data about the heaviest or lightest drink."
            
        #The history of cocktails
        elif response_data[best_index]["response_type"] == "history":
            if not cocktailss:
                if "when" not in split_message:
                    specific = input("Bot: Please give me a specific name of a cocktail:\n")
                    for x in cocktail_names:
                        if x.lower() == specific.lower():
                            out = cocktail_data[x]["History"]
                            if out:
                                return (f"{out}\n")
                            else:
                                return "I don't have the history data of this cocktail"
                    return "There is no such cocktail in my data"   
            else:   
                ans = ""
                print(f"Bot: {default_ans} {cocktailss[0]}")
                for cocktail in cocktailss:
                    if cocktail!="":
                        history_output = cocktail_data[cocktail]["History"]
                        ans += (f"{history_output}\n")
                return ans     
            
        #Exit the program                
        elif response_data[best_index]["response_type"] =="quit":
            print(f"Bot: {default_ans}")
            exit()
        else:
            return default_ans
    return default_responses.random_string()

# while True:
#     user_input = input("You: ")
#     print(get_response(user_input))