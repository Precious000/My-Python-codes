# Collections: Counter, namedtuple, OrderedDict, defaultDict, deque
from collections import Counter
a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
a = Counter("Blessing")
print(a)
a = Counter(['a', 'b', 'c', 'a', 'a', 'b', 'c', 'a'])
print(a)
a = Counter({'a': 1, 'b': '2'})
print(a)
a = Counter(cats=1, dogs=2)

# Example@
from collections import namedtuple
Grades = namedtuple('Grades', ['favor', 'Blessing'])
score = Grades(70, 60)
print(score[0])

# EXAMPLE3
from collections import OrderedDict
Report = OrderedDict()
Report['name'] = 'Darasimi'
Report['age'] = 12
Report['grade'] = 'A'
print("This is my school report", Report)

# Example4
from collections import defaultdict
A = defaultdict()
a['a'] = 1
a['b'] = 2
print(a)

# Example5
from collections import deque
a = deque()
a.append('b')
a.append('c')
print(a)
