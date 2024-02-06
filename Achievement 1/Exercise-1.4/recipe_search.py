import pickle

def display_recipe(recipe):
    print("\nRecipe:", recipe["name"])
    print("Cooking time (min):", recipe["cooking_time"])
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print("  - " + ingredient)
    print("Difficulty level:", recipe["difficulty"])

def search_ingredient(data):
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(index, ingredient)

    try:
        ingredient_searched = data["all_ingredients"][int(input("Enter the index number of the ingredient that you want to search for: "))]
    except:
        print("Warning: Input is incorrect!")
    else:
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

filename = input("Enter the recipe filename: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist")
except:
    print("An unexpected error occured.")
else:
    search_ingredient(data)