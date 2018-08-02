import requests
from json import JSONDecodeError
from time import sleep

try:
    app_id_file = open("app_id.key")
    app_id = app_id_file.read()
    app_id_file.close()
except (FileNotFoundError, IOError):
    raise FileNotFoundError("The app_id.key file was not found")    

try:
    app_key_file = open("app_key.key")
    app_key = app_key_file.read()
    app_key_file.close()
except (FileNotFoundError, IOError):
    raise FileNotFoundError("The app_key.key file was not found")    

def get_recipe_from_query(query):
    parameters = {"app_id":app_id, "app_key":app_key, "from":0, "to":1, "q":query}

    response = requests.get("https://api.edamam.com/search", params=parameters)

    try:
        data = response.json()
    except JSONDecodeError:
        return "Slow down! You are hitting the API limit. (5 requests/minute) because @dansman805#5805 is not willing to pay for a stupid joke bot"

    try:
        recipe = data["hits"][0]["recipe"]
    except IndexError:
        return "No recipe including " + query + " found."

    ingredient_list = ["Label: " + recipe["label"] + "\nURL: " + recipe["url"] + "\nImage: " + recipe["image"] + "\nIngredients:\n"]
    ingredient_list.append("``")

    for ingredient in recipe["ingredients"]:
        ingredient_list.append(ingredient["text"] + ", " + str(ingredient["weight"]) + "g\n")
    ingredient_list.append("```")

    return "".join(ingredient_list)[:-1]