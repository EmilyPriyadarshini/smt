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

a = Int('#apples')
b = Int('#bananas')
c = Int('#carrots')

s = Solver()
s.add(a+b+c == 100)
s.add(100*a + 200*b + 50*c == 10000)
s.add(And(a>0, b>0, c>0))

# Ex 03.5.a How many apples, bananas, and carrots can they buy to satisfy the previous conditions?

if (s.check() == sat):
    print(s.model())
else:
    None

# Ex 03.5.b Is there more than one way to buy the fruit satisfying the previous conditions?

s1 = Solver()
s1.add(s.assertions())
if (s1.check()==sat):
    m = s1.model()
    s1.add(Or(a!=m[a], b!=m[b], c!=m[c]))
    print("Yes, there is more than one way to buy the fruit satisfying the previous conditions: ", m)
else:
    print("No, there is NOT more than one way to buy the fruit satisfying the previous conditions")


# Ex 03.5.c If they decide to buy at least 40 bananas, are they still able to satisfy the previous conditions?

s2 = Solver()
s2.add(s.assertions())
s2.add(b>=40)
if (s2.check() ==  sat):
    print("Yes, one can satisfy the the previous conditions if they additionally want to buy at least 40 bananas", s2.model())
else:
    print("No, one CANNOT satisfy the the previous conditions if they additionally want to buy at least 40 bananas")

# Ex 03.5.d Compute how many possible combinations of apples, bananas, and carrots satisfy the initial conditions.

counter = 0

while check_and_print(s) == sat:
     counter += 1
     m = s.model()
     s.add(Or(a != m[a], b != m[b], c != m[c]))  # exclude current solution

print("The number of possible combinations of apples, bananas, and carrots that satisfy the initial conditions are:", counter)