import json
import re
from recommend_sys_util.recommend_main import recommend_cocktails

def get_response(input_string,layer,ques_type,cocktail_data, names, bot_cocktails):
    default_ans = """RECOMMEND. Please ask about
                            + cocktail recommendations
                            + ingredients in a specific cocktail
                            + taste of a specific cocktail
                            + heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                            + history of a specific cocktail
                            + or any questions related to cocktail"""

    if layer == 0:
        if ques_type in ["ingredient","taste","weight"]:
            layer +=1
            return (f"What cocktail?\nAvailable cocktails: {names}"), layer, ques_type, bot_cocktails
        else: 
            return(f"EORRRR",),layer,ques_type, bot_cocktails
    if layer == 1 and (ques_type=="ingredient" or ques_type=="taste" or ques_type=="weight"):
        if not bot_cocktails:
        # FIND AND CHECK A COCKTAIL
            split_message = re.findall(r'\b\w+\b', input_string.lower())
            # cocktail_data = load_json("history_cocktails.json")
            cocktail_names = list(cocktail_data.keys())
            cocktailss = []
            cocktail_check = {name:len(name.split()) for index,name in enumerate(cocktail_names)}
            names_tracker = list(cocktail_data.keys())
            names_tracker = [x.lower() for x in names_tracker]
            for word in split_message:
                for drink in cocktail_names:  
                    i = cocktail_names.index(drink)
                    if word.lower() in names_tracker[i].split():
                        cocktail_check[drink] -= 1
                        names_tracker[i] = names_tracker[i].replace(word.lower(),"").strip()
            for key, value in cocktail_check.items():
                if value == 0:
                    cocktailss.append(key)
        else:
            cocktailss = bot_cocktails
            bot_cocktails = ""
    #HANDLE COCKTAIL BEING GIVEN
        if cocktailss:
            if ques_type=="ingredient":
                ans=""
                for cocktail in cocktailss:
                    if cocktail!="":
                        out =', '.join(cocktail_data[cocktail]["Ingredients"])
                        ans += (f"{cocktail}\n{out}\n")
                return ans,0,"", bot_cocktails
            elif ques_type=="taste":
                ans = ""
                for cocktail in cocktailss:
                    if cocktail!="":
                        taste_output = set(cocktail_data[cocktail]["Taste"])
                        taste_output = ', '.join(list(taste_output))
                        ans += (f"{cocktail}\n{taste_output}\n")
                return ans,0,"", bot_cocktails
            elif ques_type=="weight":
                hea = "Heavy: "
                lig = "Light: "
                for cocktail in cocktailss:
                    if cocktail!="":
                        weight_output = cocktail_data[cocktail]["Weight"]
                        if weight_output.lower()=="heavy":
                            hea += (f" {cocktail}")
                        elif weight_output.lower()=="light":
                            lig += (f" {cocktail}")
                if lig =="Light: ":
                    return (f"""
                            {hea}
                            """),0,"", bot_cocktails
                if hea =="Heavy: ":
                    return (f"""
                            {lig}
                            """),0,"", bot_cocktails
                return (f"""
                        {hea}
                        {lig}
                        """),0,"", bot_cocktails
        else:
            return (f"""Invalid cocktail(s). {default_ans}"""),0,"", bot_cocktails
    else:
        return (f"""Can't understand that! {default_ans}"""), 0,"", bot_cocktails




    