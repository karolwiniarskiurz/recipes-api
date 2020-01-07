def is_recipe_owner(recipe, user):
    return recipe.user_id == user.id
