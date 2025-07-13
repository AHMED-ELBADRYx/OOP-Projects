# Collection of recipes by class

class Recipe:
    def __init__(self, name, ingredients, time, method):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.method = method
    
    def print_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Time: {self.time}")
        print(f"Method: {self.method}")

def get_input():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients: ")
    time = input("Enter cooking time: ")
    method = input("Enter cooking method: ")
    return Recipe(name, ingredients, time, method)

print("Welcome to the recipe collection! 🍳🧑‍🍳")

recipe = get_input()

print("-" * 30)
recipe.print_recipe()
print("-" * 30)