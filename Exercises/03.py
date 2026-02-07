from z3 import *
from utils import *

# 03.1 
# Find the smallest integer that can be written as a sum of two squares in two different ways


# 03.2 
# Find the integer between 150 and 200 that can be written in the most different ways as a sum of two squares
# If there is more then one such integer, find the smallest one

# 03.3
# Find the closest point to the origin that satisfies the following constraints:
# x**2 + y**2 < 3
# y >= x**2 + 1

x = Real('x')
y = Real('y')
s = Solver()
s.add(x**2 + y**2 < 3)
s.add(y >= x**2 + 1)

has_solution = check_and_print(s)

while check_and_print(s) == sat:
    m = s.model()
    s.add(x**2 + y**2 < m[x]**2 + m[y]**2)

# 03.4
# Find the closest point to the origin that satisfies the following constraints:
# x**2 + y**2 < 3
# y > x**2 + 1

x = Int('x')
y = Int('y')
s = Solver()
s.add(x**2 + y**2 < 3)
s.add(y > x**2 + 1)

has_solution = check_and_print(s)

while check_and_print(s) == sat:
    m = s.model()
    s.add(x**2 + y**2 < m[x]**2 + m[y]**2)

# 03.5
# Gavina and Gavino go to San Benedetto market to buy apples, bananas, and carrots.
# They want to buy exactly 100 fruits, spending exactly 100€.
# They want to buy at least 1 apple, 1 banana, and 1 carrot.
# 1 banana costs 2€ (inflation...)
# 1 apple costs 1€
# 1 carrot costs 50c
#
# Ex 03.5.a How many apples, bananas, and carrots can they buy to satisfy the previous conditions?
# Ex 03.5.b Is there more than a way to buy the fruit satisfying the previous conditions?
# Ex 03.5.c If they decide to buy at least 40 bananas, are they still able to satisfy the previous conditions?
# Ex 03.5.d Compute how many possible combinations of apples, bananas, and carrots satisfy the initial conditions.

a = Int('apple')
b = Int('banana')
c = Int('carrot')
#e = Int("Euro")

s = Solver()
s.add(a+b+c == 100)
s.add(a>1 & b>1 & c>1)
