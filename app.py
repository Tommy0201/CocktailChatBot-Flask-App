from flask import Flask, render_template, request
from chat import get_response
from detect_input import response_classifier
import json
from recommend_sys_util.recommend_main import recommend_cocktails

app = Flask(__name__)
layer = 0
ques_type=""
conversation = []
cached_cocktail_data={}
with open("history_cocktails.json", encoding='utf-8') as bot_responses:
    cached_cocktail_data = json.load(bot_responses)
cocktail_name = ""
for ind,key in enumerate(cached_cocktail_data):
    if ind != (len(cached_cocktail_data)-1):
        cocktail_name = cocktail_name + key + ", "
    else:
        cocktail_name = cocktail_name + key + " "
print(f"cocktail_name: {cocktail_name}")
        
default_system_response = """Please ask about
                            + cocktail recommendations
                            + ingredients in a specific cocktail
                            + taste of a specific cocktail
                            + heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                            + history of a specific cocktail
                            + or any questions related to cocktail"""


@app.route('/')


def index():
    global conversation
    global layer 
    global ques_type
    global bot_response
    global bot_cocktails
    layer = 0
    ques_type = ""
    bot_response = ""
    bot_cocktails = ""
    conversation.clear()
    begin_message = "Hey, my name is Coco. I am a Cocktail Chatbot. " + default_system_response
    conversation.append(("System", begin_message))
    return render_template('index.html', conversation=conversation, cocktail_name=cocktail_name)

@app.route('/read_more', methods=['POST'])
def read_more():
    global conversation
    store = request.form['store']
    conversation = conversation[:-1]
    conversation.append(("System", store))
    return render_template('index.html', conversation=conversation)


@app.route('/', methods=['POST'])
def chat():
    global conversation
    global layer
    global ques_type
    global bot_response
    global bot_cocktails
    user_input = request.form['user_input']
    if layer == 0 and ques_type == "":
        bot_response,ques_type, layer, bot_cocktails = response_classifier(user_input,ques_type,layer,bot_cocktails)
        print(f"""
              bot response: {bot_response}
              layer: {layer}
              question type: {ques_type}
              bot_cocktail: {bot_cocktails}
              """)
        taste = ["bitter","spicy","sour","salty","sweet","heavy","light","strong"]
        taste_ask = False
        for x in taste:
            if x in user_input.lower():
                taste_ask = True
                break
        print(f"taste ask: {taste_ask}")
        if (bot_response not in ["0","1","2","3"]):
            if ques_type != "other" and taste_ask == False:
                bot_response = "Invalid input! " + default_system_response                
            layer = 0 
            ques_type = ""
            conversation.append(("You", user_input))
            conversation.append(("System", bot_response))
            return render_template('index.html', conversation=conversation)
    if ques_type == "recommend":
        system_response, layer,ques_type = recommend_cocktails(user_input,layer,ques_type)
    else:        
        system_response, layer,ques_type, bot_cocktails = get_response(user_input, layer,ques_type,cached_cocktail_data,cocktail_name,bot_cocktails)
    if len(system_response) > 100 and ("What cocktail?" in system_response):
        store = system_response
        truncated_response = system_response[:100] + "..."
        read_more_link = '<form action="/read_more" method="POST"><input type="hidden" name="store" value="' + store + '"><input type="submit" value="Read More"></form>'
        system_response = truncated_response + read_more_link
    # print(f"layer:{layer}")
    # print(f"question type: {ques_type}")
    conversation.append(("You", user_input))
    conversation.append(("System", system_response))
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
