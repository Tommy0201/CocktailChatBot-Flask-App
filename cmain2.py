def get_response(input_string, layer):
    if input_string == "1" and layer == 0:
        layer += 1
        return "What cocktail history would you like to learn about?", layer    
    elif layer == 1:
        layer = 0
        if input_string == "gin":
            return "the history of gin start with...", layer
        else:
            return "no data available", layer