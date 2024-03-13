import random


def random_string():
    random_list = [
        """I can't answer that, please check your spelling and try asking these topics instead:
        1) ingredients in a specific cocktail
        2) taste of a specific cocktail
        3) heaviness/lightness of a cocktail or comparing the weight among different given cocktails
        4) history of a specific cocktail
        5) cocktail recommendations."""
    ]

    return random_list[random.randrange(len(random_list))]