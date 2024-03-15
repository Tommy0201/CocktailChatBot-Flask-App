from flask import Flask, render_template, request
from cmain import get_response 

app = Flask(__name__)
a=1
conversation = []
@app.route('/')
def index():
    global conversation
    conversation.clear()
    return render_template('index.html', conversation=conversation)

@app.route('/', methods=['POST'])
def chat():
    global conversation
    user_input = request.form['user_input']
    system_response = get_response(user_input)
    conversation.append(("You", user_input))
    conversation.append(("System", system_response))
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
