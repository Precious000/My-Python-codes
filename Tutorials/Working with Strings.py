# Working with String: ordered, immutable
my_string = """Hello
World"""
print(my_string)

# Accessing a string with slice
my_string = 'Hello world'
result = my_string[2]
print(result)

# Concatenating strings
Greeting = "Hello"
name = "precious"
result = Greeting + " " + name
print(result)

# changing to upper or lower characters
my_string = 'Hello world'
print(my_string.upper())
"""lower"""
my_string = "Hello world"
print(my_string.lower())
# Checking for a character
my_string = 'Hello world'
food = {'kind': 'rice', 'Quantity': [2, 3]}
print(food)
food.pop('kind')
print(food)

food_cpy = food
print(food_cpy)
food_cpy['expr'] = 'july'
print(food_cpy)
