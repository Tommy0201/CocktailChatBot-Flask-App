import json
import re
from recommend_sys.input2 import recommend_cocktails

def get_response(input_string,layer,ques_type,cocktail_data):
    # def load_json(file, encoding='utf-8'):
    #     with open(file, encoding='utf-8') as bot_responses:
    #         print(f"Loaded '{file}' successfully!")
    #         return json.load(bot_responses)
        #GREETING, NAMNIG, JOB, QUIT
    default_ans = """Please press:
                <span style="color: yellow;">0</span> for cocktail recommendations
                <span style="color: yellow;">1</span> for ingredients in a specific cocktail
                <span style="color: yellow;">2</span> for taste of a specific cocktail
                <span style="color: yellow;">3</span> for heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                <span style="color: yellow;">4</span> for history of a specific cocktail"""

    output_string,layer,ques_type = recommend_cocktails(input_string,layer,ques_type)
    if output_string != "invalid":
        return output_string,layer,ques_type
    if layer == 0:
        if input_string == "1":
            layer +=1
            ques_type = "ingredient"
            return ("What cocktail? "), layer, ques_type
        elif input_string == "2":
            layer +=1
            ques_type = "taste"
            return "What cocktail? ", layer, ques_type
        elif input_string == "3":
            layer +=1
            ques_type = "weight"
            return "What cocktail? ", layer, ques_type
        elif input_string == "4":
            layer +=1
            ques_type = "history"
            return "What cocktail? ", layer, ques_type
    if layer == 1 and (ques_type=="ingredient" or ques_type=="taste" or ques_type=="weight" or ques_type=="history"):
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
    #HANDLE COCKTAIL BEING GIVEN
        if cocktailss:
            if ques_type=="ingredient":
                ans=""
                for cocktail in cocktailss:
                    if cocktail!="":
                        out =', '.join(cocktail_data[cocktail]["Ingredients"])
                        ans += (f"{cocktail}\n{out}\n")
                return ans,0,""
            elif ques_type=="taste":
                ans = ""
                for cocktail in cocktailss:
                    if cocktail!="":
                        taste_output = set(cocktail_data[cocktail]["Taste"])
                        taste_output = ', '.join(list(taste_output))
                        ans += (f"{cocktail}\n{taste_output}\n")
                return ans,0,""
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
                            """),0,""
                if hea =="Heavy: ":
                    return (f"""
                            {lig}
                            """),0,""
                return (f"""
                        {hea}
                        {lig}
                        """),0,""
            elif ques_type=="history":
                    ans = ""
                    for cocktail in cocktailss:
                        if cocktail !="":
                                out =  cocktail_data[cocktail]["History"]
                                ans += (f"{cocktail}\n{out}\n")
                    if ans:
                        return ans, 0, ""
                    else:
                        return "There is no history of this cocktail",0,""
        else:
            return "Invalid cocktail(s)",0,""

    else:
        return (f"""Can't understand that! Please restart!
                   {default_ans}"""), 0,""




    