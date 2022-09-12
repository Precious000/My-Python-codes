# Sets: mutable, No Duplicate, unordered
my_set_funct = {1, 2, 4, 5}
print(my_set_funct)
# Example2
my_set_funct = set([1, 2, 3, 4])
print(my_set_funct)
# Adding & Removing elements in an empty set
my_set_funct = set()

my_set_funct.add(1)
my_set_funct.add(2)
my_set_funct.add(3)
my_set_funct.add(5)

my_set_funct.remove(5)
my_set_funct.discard(30)
print(my_set_funct)

# using loop in a set
my_set_funct = set()

my_set_funct.add(1)
my_set_funct.add(2)
my_set_funct.add(3)
my_set_funct.add(5)
for s in my_set_funct:
    print(s)

if 2 in my_set_funct:
    print("This is my lucky number")
