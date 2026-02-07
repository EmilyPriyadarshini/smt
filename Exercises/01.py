
# 01.1
# Check if the following system of equations has a solution for x and y Real numbers:
#
#   x + y + 10 = 3
#   8 = y - x

from z3 import *

x = Real('x')
y = Real('y')

c1 = x + y + 10 == 3
c2 = 8 == y - x

s = Solver()
s.add(c1)
s.add(c2)

print(f"\nCheck 1: \t{s.check()}")

# 01.2 
# Check if the previous system has a solution for x and y Integer numbers

x1 = Int('x')
y1 = Int('y')

c3 = x1 + y1 + 10 == 3
c4 = 8 == y1 - x1

s1 = Solver()
s1.add(c3)
s1.add(c4)

print(f"\nCheck 2: \t{s1.check()}")

# 01.3
# Check if the previous system of equations has a solution if we add the following inequality,
# both for the case in which x and y Real, and in the case in which they are Integers:
#
#   x > y

c5 = x > y

s.add(c5)
s1.add(c5)

print(f"\nCheck 3.1: \t{s.check()}")
print(f"\nCheck 3.2: \t{s1.check()}")


# 01.4
# Check if there exists Boolean values b1, b2, b3 such that:
#   (b1 OR b2) AND ((NOT b2) OR b3)

b1 = Bool('b')
b2 = Bool('b')
b3 = Bool('b')

c6 = And(Or(b1,b2),Or(b3,Not(b2)))

s3 = Solver()
s3.add(c6)
print(f"\nCheck 4: \t{s3.check()}")

# 01.5
# Check if the following formula is satisfiable:
#
#       ((b AND x > 10) OR (x > 3 AND y > 4)) 
#   AND ((x + y)**2 == 20)
#   AND (NOT(b) OR y > 10)
#   
# where x and y are Real variables and b is a Boolean variable.

b = Bool('b')

c7 = Or(And(b,x>10),And(x>3,y>4))
c8 = (x + y)**2 == 20
c9 = Or(Not(b),y>10)

c10 = And(c7,c8,c9)

s4 = Solver()
s4.add(c10)
print(f"\nCheck 5: \t{s4.check()}")


# 01.6
# Same as 01.5 but switch the last occurrence of "NOT(b)" with "b"

c9_1 = Or(b,y>10)

c10_1 = And(c7,c8,c9_1)

s5 = Solver()
s5.add(c10_1)
print(f"\nCheck 6: \t{s5.check()}")

# 01.7
# Prove that NOT(p AND q) implies (NOT p) OR (NOT q)

p = Bool('b')
q = Bool('b')

c11 = Not(And(p,q))
c12 = Or(Not(p),Not(q))
c13 = Not(Implies(c11,c12))

s6 = Solver()
s6.add(c13)
print(f"\nCheck 7: \t{s6.check()}")

# 01.8
# Prove that NOT(p AND q) *does not* imply (NOT p) AND (NOT q)

c14 = Not(And(Not(p),Not(q)))
c15 = Implies(c11,c14)

s7 = Solver()
s7.add(c15)
print(f"\nCheck 8: \t{s7.check()}")