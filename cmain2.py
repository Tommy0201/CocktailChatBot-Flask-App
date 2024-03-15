
def get_response(input_string):
    if input_string == "1":
        user_input = input("What cocktail history would you like to learn about?")
        if user_input == "gin":
            return "the history of gin start with..."
        else:
            return "no data available"
    