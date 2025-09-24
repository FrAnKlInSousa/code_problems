def pete_the_baker(recipe: dict, ingredients: dict):
    max_recipe = None
    available_ingredients = set(ingredients.keys())
    necessary_ingredients = set(recipe.keys())
    # check if any ingredients are missing
    if len(available_ingredients - necessary_ingredients) != len(
        available_ingredients
    ) - len(necessary_ingredients):
        return 0
    for ingredient, quantity in recipe.items():
        for available_ingredient, available_quantity in ingredients.items():
            if available_ingredient == ingredient:
                if (
                    max_recipe is None
                    or (available_quantity // quantity) < max_recipe
                ):
                    max_recipe = available_quantity // quantity

    return max_recipe
