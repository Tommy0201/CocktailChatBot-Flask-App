from flask import Flask, render_template, request
from cmain import get_response  # Assuming get_response is your function to generate system responses

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', conversation=[])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    system_response = get_response(user_input)
    conversation = request.form.getlist('conversation[]')
    conversation.append(("You", user_input))
    conversation.append(("System", system_response))
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
