import re

def cocktail_detector(input_string, names):
    split_message = re.findall(r'\b\w+\b',input_string.lower())
    print(f"split_message: {split_message}")
    # cocktail_data = load_json("history_cocktails.json")
    # cocktail_names = list(cocktail_data.keys())
    cocktailss= []
    names_tracker = names.lower().split(",")    

    cocktail_names = names.lower().split(",")
    print(f"cocktail_names: {cocktail_names}")
    print(f"type of name_slitting: {type(cocktail_names)}")
    cocktail_check = {name:len(name.strip().split(" ")) for name in cocktail_names}
    print(f"cocktail_check: {cocktail_check}")
    # names_tracker = list(cocktail_data.keys())
    for word in split_message:
        for i, drink in enumerate(cocktail_names): 
            if word in names_tracker[i].split():
                # print(f"names_tracker{i} before: {names_tracker[i]}")
                cocktail_check[drink] -= 1
                names_tracker[i] = names_tracker[i].replace(word.lower(),"").strip()
                # print(f"names_tracker{i} after: {names_tracker[i]}")
    for key, value in cocktail_check.items():
        if value == 0:
            cocktailss.append(key)
    print(f"cocktailss: {cocktailss}")
            

import requests

def get_latest_version(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    else:
        return None

packages = ["openai", "pandas","python-dotenv","flask","scikit-learn","numpy"]

  
if __name__ == "__main__":
    # input_string = "old    fashioned,    martini"
    # names = "Monkey Gland, Mitch Martini, Painkiller, Brandy Alexander, Japanese Slipper, Greyhound, Hedgerow Sling, Caiparissima, Lynchburg Lemonade, The Gold Record, Tequila Sunrise, John Collins, Dubonnet, Sex On The Beach, Lemon Drop, Bijou, Whiskey Mac, Martinez, Calvados Old Fashioned, Blood & Sand, Red Snapper, Boulevardier, Bees Knees, Rusty Nail, Gin Rickey, Rum Old Fashioned, Caiprioska, Jungle Bird, Brooklyn, Sangria, Navy Grog, Hot Buttered Rum, Bronx, Irish Coffee, Grasshopper, Corpse Reviver No2, Hurricane, Sidecar, Batida, Champagne, Southside, Mimosa, Penicillin, El Diablo, Gibson, Ramos Gin Fizz, Singapore Sling, Pina Colada, Mint Julep, Blue Blazer, Breakfast Martini, Hot Toddy, Clover Club, Zombie, Americano, Cubre Libre, Seabreeze, Anejo Highball, Aviation, Rum Swizzle, Planter's Punch, Bramble, French 75, White Russian, Elderflower Collins, Gimlet, Pisco Sour, Tom Collins, Long Island Iced Tea, Kir Royale, Sazerac, Pimm's Cup, Cosmopolitan, Bellini, Vesper Martini, Hemingway Daiquiri, Mai Tai, Paloma, Tommy's Margarita, Bloody Mary, Vodka Martini, Amaretto Sour, Caipirinha, Manhattan, Moscow Mule, French Martini, Whiskey Sour, Dark 'n' Stormy, Martini, Margarita, Mojito, Daiquiri, Aperol Spritz, Negroni, Pornstar Martini, Espresso Martini, Old Fashioned, Screwdriver, Gin & Tonic"
    # cocktail_detector(input_string,names)  
    with open("requirements.txt", "w") as file:
        for package in packages:
            version = get_latest_version(package)
            if version:
                file.write(f"{package}=={version}\n")
            else:
                print(f"Could not fetch version for {package}")      
        
