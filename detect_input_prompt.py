DETECT_COCKTAIL = """

You are an expert in cocktail extracting and comparing cocktail extracted with a given list.

Given a list of cocktail {cocktail_default}

And given a user's response: {user_response}

OUTPUT IN JSON FORMAT BELOW (NO EXPLANATION/EXTRA WORDS ALLOWED):

{{
    "cocktail": [],
    "cocktail_in_list": []
}}

INSTRUCTION: 

Step 1:  extract the cocktail name from user's response and if it exsit, fill out the "cocktail" value. If it does not exist then return empty array for both keys "cocktail" and "cocktail_in_list"
Step 2: check if extracted cocktail is also in the given list of cocktail. If it is then set cocktail value to be the value extracted. If not then set it to be an empty array

Example 1: "B52 is a good cocktail" must output 
{{
    "cocktail": ["B52"],
    "cocktail_in_list": None, 
}}
Explanation: "B52" is a cocktail. However "B52" is not in the list {cocktail_default}

Please think step by step. 
"""

DETECT_INPUT = """
You are an intent extractor. You are given a user's response asking about cocktails in general:
{user_response}

Your job is to categorize if this user's response belongs to number 0, 1, 2, 3  or -1. 

Output in JSON String format below:
{{
    "number": int(), 
    "bot-answer": "",
}}
 
FOLLOW THIS INSTRUCTION:

Step 1: Filling out value of "number"
    If user's answer is about cocktail recommendation ("recommend cocktail", "suggest me a cocktail", "suggest drinks", "can you recommend me a good cocktail", etc...) set value of "number" to 0
        However, if user's answer is about cocktail recommendation and taste preference were recommended ("recommend me a cocktail that is sweet","I want to drink something light","I want to have a spicy and sour drink, can u recommend?", etc...), set value of "number" to 4 instead of 0
    If user's answer is about ingredients of a cocktail ("what is in [cocktail]?", "what does [cocktail] contain?", "what are the ingredients of [cocktail]?" etc...)  set value of "number" to 1
    If user's answer is about tastes of a drink such as ("what does [cocktail] taste like?", "the taste of [cocktail]", etc...) set value of "number" to 2
    If user's answer is about weight of a cocktail: ("how heavy is [cocktail]?", "is [cocktail] a light drink?", etc...) set value of "number" to 3
    If user's answer is none of the above but it is still about cocktails ("what the history of [cocktail]?", "what is the color of [cocktail]?", "how expensive is [cocktail]?","is [cocktail] red?" etc...), set value of "number" to 4
    Otherwise, if user's answer is irrelavant ("what is the color of the sky?", "ok", "saikasdjvp", random characters, etc...) please set the value of "number" to be -1.
Step 2: Filling out value of "bot-answer"
    Set value of "bot-answer" to be your own answer assuming that you are a cocktail/mixologist expert. Please only answer the question of user, do not ask follow up question.
    if you cannot answer, set the value of "bot-answer" to be ""

Please think step by step.
"""

COCKTAIL_DEFAULT = """
Monkey Gland, Mitch Martini, Painkiller, Brandy Alexander, Japanese Slipper, Greyhound, Hedgerow Sling, Caiparissima, Lynchburg Lemonade, The Gold Record, Tequila Sunrise, John Collins, Dubonnet, Sex On The Beach, Lemon Drop, Bijou, Whiskey Mac, Martinez, Calvados Old Fashioned, Blood & Sand, Red Snapper, Boulevardier, Bees Knees, Rusty Nail, Gin Rickey, Rum Old Fashioned, Caiprioska, Jungle Bird, Brooklyn, Sangria, Navy Grog, Hot Buttered Rum, Bronx, Irish Coffee, Grasshopper, Corpse Reviver No2, Hurricane, Sidecar, Batida, Champagne, Southside, Mimosa, Penicillin, El Diablo, Gibson, Ramos Gin Fizz, Singapore Sling, Pina Colada, Mint Julep, Blue Blazer, Breakfast Martini, Hot Toddy, Clover Club, Zombie, Americano, Cubre Libre, Seabreeze, Anejo Highball, Aviation, Rum Swizzle, "Planters Punch", Bramble, French 75, White Russian, Elderflower Collins, Gimlet, Pisco Sour, Tom Collins, Long Island Iced Tea, Kir Royale, Sazerac, "Pimms Cup", Cosmopolitan, Bellini, Vesper Martini, Hemingway Daiquiri, Mai Tai, Paloma, "Tommys Margarita", Bloody Mary, Vodka Martini, Amaretto Sour, Caipirinha, Manhattan, Moscow Mule, French Martini, Whiskey Sour, "Dark n Stormy", Martini, Margarita, Mojito, Daiquiri, Aperol Spritz, Negroni, Pornstar Martini, Espresso Martini, Old Fashioned, Screwdriver, Gin & Tonic
"""

