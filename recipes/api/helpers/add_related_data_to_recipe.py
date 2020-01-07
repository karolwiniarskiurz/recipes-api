def add_related_data_to_recipe(data, serializer_class, recipe_id):
    for datum in data:
        datum['recipe'] = recipe_id
    serializer = serializer_class(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        raise Exception(serializer.errors)
