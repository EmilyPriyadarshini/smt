
# 02.1
# Do the following two curves intersect? If yes, in which points?
#   y = x**2
#   y = 2*x + 3

from z3 import *
from utils import *
set_param(proof=True)

# check if set_param is set to true
print(f"Proof generation is set to: {get_param('proof')}")

x = Real('x')
y = Real('y')

c1 = y == x**2
c2 = y == 2*x + 3

s = Solver()
s.add(c1)
s.add(c2)

print(f"\nCheck 1: \t{s.check()}")
print(f"Model 1: \t{s.model()}")

# 02.2
# Do the following two circumferences intersect? If yes, in which points?
#   x**2 + y**2 = 13
#   (x-5)**2 + (y-5)**2 = 5

c3 = x**2 + y**2 == 13
c4 = (x-5)**2 + (y-5)**2 == 5

s1 = Solver()
s1.add(c3)
s1.add(c4)

print(f"\nCheck 2: \t{s1.check()}")

# 02.3
# Prove that NOT(p AND q) implies (NOT p) OR (NOT q), providing a formal proof 

p = Bool('b')
q = Bool('b')

c5 = Not(And(p,q))
c6 = Or(Not(p),Not(q))
c7 = Not(Implies(c5,c6))

s2 = Solver()
s2.add(c7)
print(f"\nCheck 3: \t{s2.check()}")
#print(f"\nProof 3: \t{s2.proof()}")


# 02.4
# Prove that NOT(p AND q) *does not* imply (NOT p) AND (NOT q), providing a concrete counterexample

# c8 = And(Not(p),Not(q))
# c9 = Implies(c5_1,c8)

# s3 = Solver()
# s3.add(c9)
# print(f"\nCheck 4: \t{s3.check()}")
# print(f"\nProof 4: \t{s3.proof()}")

# 02.5
# Do the following two lines intersect if x is in the interval [-10, 10]? 
# If yes, in which points? If no, why?
# x = y
# 3x = y + 25




# 02.6
# Write a function that takes as input an integer n
# and finds positive integers a, b such that a**2 - b**2 = n.

a = Int('a')
b = Int('b')
n = Int('n')

def diffOfSquares(n):
    return Solver.model(a**2 - b**2 == n)
        
#diffOfSquares(123)


# 02.7
# Write a function that takes as input an integer n
# and finds positive integers a, b such that a**2 + b**2 = n.
"""
def sumOfSquares(n_input):
.   ...
        
sumOfSquares(123)
sumOfSquares(12345)
sumOfSquares(-12)
"""

# 02.8 Find an integer greater than 90 that can be written as a sum of squares 

# 02.9 Find the smallest integer greater than 130 that can be written as a sum of squares

# 02.10
# Write a function that takes as input a positive integer n
# and checks whether n is a prime. 
# If n is not a prime, the function should print some information 
# that proves that n is not a prime.
"""
def isPrime(n_input):

isPrime(12345)
"""


# 02.11
# Write a function that takes as input two positive integers a, b,
# and checks whether a and b can be part of a Pythagorean triple.

"""
def arePartOfPythagorean(a_input, b_input):
    ...

arePartOfPythagorean(12, 35) # expected: sat
arePartOfPythagorean(33, 65) # expected: sat
arePartOfPythagorean(89, 39) # expected: sat
arePartOfPythagorean(89, 139) # expected: unsat
arePartOfPythagorean(45, 824) # expected: unsat
"""



# 02.12 Find in how many different ways 128 can be written as a sum of squares