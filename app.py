from flask import Flask, render_template, request
from cmain3 import get_response
import json

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


@app.route('/')


def index():
    global conversation
    global layer 
    global ques_type
    layer = 0
    ques_type = ""
    conversation.clear()
    default_system_response = """Hey, my name is Coco. I am a Cocktail Chatbot. Please enter
                                <span style="color: yellow;">0</span> for cocktail recommendations
                                <span style="color: yellow;">1</span> for ingredients in a specific cocktail
                                <span style="color: yellow;">2</span> for taste of a specific cocktail
                                <span style="color: yellow;">3</span> for heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                                <span style="color: yellow;">4</span> for history of a specific cocktail"""

    conversation.append(("System", default_system_response))
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
    user_input = request.form['user_input']
    system_response, layer,ques_type = get_response(user_input, layer,ques_type,cached_cocktail_data,cocktail_name)
    if len(system_response) > 100 and ("What cocktail?" in system_response):
        store = system_response
        truncated_response = system_response[:100] + "..."
        read_more_link = '<form action="/read_more" method="POST"><input type="hidden" name="store" value="' + store + '"><input type="submit" value="Read More"></form>'
        system_response = truncated_response + read_more_link
    print(f"layer:{layer}")
    print(f"question type: {ques_type}")
    conversation.append(("You", user_input))
    conversation.append(("System", system_response))
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
