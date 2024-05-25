from sets_categories_data import (ALCOHOLS)


def clean_ingredients(plato, ingredientes):
    ingredientes_clean = set(ingredientes)

    return (plato,ingredientes_clean)



def check_drinks(bebida, ingredientes):
    contiene_alcohol= False
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            contiene_alcohol = True
            break
    if contiene_alcohol:
        return f"{bebida} Cocktail"
    else:
        return f"{bebida} Mocktail"
