## Overview
The recommend_sys folder containing the original recommendation function of the chatbot, which taking in ingredients, taste, and heaviness of the drink based on the user's input and then output top 5 closest cocktails that resemeble those requirments.

The other part are flask app, seeking to answer other questions such as: history of the cocktail, taste of the cocktail, heaviness/lightness of a cocktail 

## How to run 
Make sure that you have installed Flask app by running:
    pip install flask
Fill in your OpenAI API Key by creating your .env file

Go to app.py and run this line in the command line
    python app.py
