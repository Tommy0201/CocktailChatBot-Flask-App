import pandas as pd
from openai import OpenAI
import json
from detect_input_prompt import DETECT_INPUT, COCKTAIL_DEFAULT, DETECT_COCKTAIL
from dotenv import load_dotenv
import os

#Working with OPENAI API
load_dotenv()

client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY'),
)

def detect_intent(user_response):
    payload = {
        "user_response": user_response,
        "cocktail_default": COCKTAIL_DEFAULT,
    }
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = [
            {"role": "system","content": DETECT_INPUT.format(**payload)},
        ],
    )
    output = response.choices[0].message.content
    print("detect intent: ",output)
    print("type of detect intent:",type(output))
    return output

def detect_cocktail(user_response):
    payload = {
        "user_response": user_response,
        "cocktail_default": COCKTAIL_DEFAULT,
    }
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = [
            {"role": "system","content": DETECT_COCKTAIL.format(**payload)},
        ],
    )
    output = response.choices[0].message.content
    print("detect_cocktail ", output)
    print(type(output))
    return output

def response_classifier(user_response, ques_type, layer, cocktails_in_list):
    c = detect_cocktail(user_response)
    try:
        cocktail_dict = json.loads(c)
    except json.JSONDecodeError as e:
        print("JSON decoding failed for cocktail_dict:", e)
        cocktail_dict = {}
    i = detect_intent(user_response)
    try:
        intent_dict = json.loads(i)
    except json.JSONDecodeError as e:
        print("JSON decoding failed for intent_dict:", e)
        intent_dict = {}
    print("intent_dict: ",intent_dict)
    if cocktail_dict:
        cocktails = cocktail_dict.get("cocktail")
        cocktails_in_list = cocktail_dict.get("cocktail_in_list")
    else:
        cocktails, cocktails_in_list = [], []
    if intent_dict:
        intent_num = intent_dict.get("number")
        bot_answer = intent_dict.get("bot-answer")
    else:
        intent_num, bot_answer = -1, ""
    if intent_num == 0 or intent_num == 1 or intent_num == 2 or intent_num == 3:
        new_dict= {0:"recommend",1:"ingredient",2:"taste",3:"weight"}
        if cocktails_in_list and len(cocktails_in_list) == len(cocktails):
            ques_type = new_dict[intent_num]
            layer = 1
            return str(intent_num), ques_type, layer, cocktails_in_list
        elif not cocktails_in_list and not cocktails: 
            ques_type = new_dict[intent_num]
            layer = 0
            taste = ["bitter","spicy","sour","salty","sweet","heavy","light","strong"]
            taste_ask = False
            for x in taste:
                if x in user_response.lower():
                    taste_ask = True
                    break
            if taste_ask == True:
                return bot_answer, ques_type, layer, cocktails_in_list
            return str(intent_num), ques_type, layer, cocktails_in_list
            
        else:
            return bot_answer, ques_type, layer, cocktails_in_list
    elif intent_num == 4:   
        ques_type = "other"
    return bot_answer, ques_type, layer, cocktails_in_list


# detect_cocktail("what does the taste of Rum Swizzle, French 75, B52 cocktail like?")
# detect_input("what does the taste of Banshee cocktail like? ","",0)

# Các trường hợp: 
# + TH 1: cocktail k thuộc cocktail_in_list, co cocktal intent thuộc --> bot tự trả lời
# + TH 2: cocktail thuộc list, intent sai -> bot tự trả lời 
# + TH 3: k có cocktail, intent sai --> bot tự trả lời 
# + Th 4: cocktail k thuộc, intent sai --> bot 
# + TH 5: cocktail thuộc cocktail in list và có cả k thuộc, intent thuoc --> bot tự trả lời 

# + TH 3: cocktail thuộc list, và k có cocktail nào khác, intent đúng --> dẫn đến layer 1, quest type = intent
# + TH 2: k có cocktail, intent thuộc 0/1/2/3 -> dẫn đến layer 0, questype = intent
