## Overview
The recommend_sys folder containing the original recommendation function of the chatbot, which taking in ingredients, taste, and heaviness of the drink based on the user's input and then output top 5 closest cocktails that resemeble those requirments.

The other part are flask app, seeking to answer other questions such as: history of the cocktail, taste of the cocktail, heaviness/lightness of a cocktail, or any relevant questions

## How to run 
Make sure that you have "pip" installed. After that type in the VS command:
    pip install -r requirements.txt
    
Create your own .env file and fill in the
    OPENAI_API_KEY= your-api-key

After that, run this in the command line
    python app.py
