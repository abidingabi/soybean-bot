from random import choice
from data_retrieval import get_recipe_from_query

# Foods in foods.txt taken from http://eatingatoz.com/food-list/
food_file = open("foods.txt", "r")

foods = food_file.readlines()

food_file.close()

def get_recipe():
    return get_recipe_from_query(choice(foods)[:-1])
