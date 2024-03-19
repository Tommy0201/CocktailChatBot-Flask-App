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


@app.route('/')
def index():
    global conversation
    conversation.clear()
    default_system_response = """Hey, my name is Coco. I am a Cocktail Chatbot. Please enter
                                <span style="color: yellow;">0</span> for cocktail recommendations
                                <span style="color: yellow;">1</span> for ingredients in a specific cocktail
                                <span style="color: yellow;">2</span> for taste of a specific cocktail
                                <span style="color: yellow;">3</span> for heaviness/lightness of a cocktail or comparing the weight among different given cocktails
                                <span style="color: yellow;">4</span> for history of a specific cocktail"""

    conversation.append(("System", default_system_response))
    return render_template('index.html', conversation=conversation)

@app.route('/', methods=['POST'])
def chat():
    global conversation
    global layer
    global ques_type
    user_input = request.form['user_input']
    system_response, layer,ques_type = get_response(user_input, layer,ques_type,cached_cocktail_data)
    print(f"layer:{layer}")
    print(f"question type: {ques_type}")
    conversation.append(("You", user_input))
    conversation.append(("System", system_response))
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
