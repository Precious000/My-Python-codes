# Working with Dictionary
food = {'kind': 'rice', 'Quantity': [2, 3]}
print(food)
for f in food.keys():
    print(f)
    if "kind" in food:
        print(food["kind"])
    else:
        print("Requested item not in the list")

# Updating my dictionary
food = {'kind': 'rice', 'Quantity': [2, 3]}

food2 = {'kind': 'rice', 'Quantity': [2, 3], 'exp': 'July', 'Time_of_expy': '7:30pm'}

food2.update(food)
print(food2)