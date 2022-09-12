# Lambda arguments: expression,map,reduce
add_num= lambda x, y: x + y
print(add_num(5, 3))

# Ex
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda x: x+2, lists)
print(list(result))
# ex
from functools import reduce
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x+y, lists)
print(result)

# Examp
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lists.remove(1)
print(lists)
