
# 04.1 (Die Hard 3 water pouring puzzle)
# You have a 3-gallon jug and a 5-gallon jug, and an unlimited supply of water (but no measuring cups).
# You can fill up a jug, empty a jug, or pour water from one jug to the other until either the first jug is empty or the second jug is full.
# You need to measure out exactly 4 gallons of water.
# How can you do it?
# Write a Bounded Model Checking procedure to solve this problem.


# 04.2 (Parametric Die Hard 3 water pouring puzzle)
# You have a n1-gallon jug and a n2-gallon jug.
# You need to measure out exactly n3 gallons of water.
# Write a Bounded Model Checking procedure that can solve this problem for every instance of (n1, n2, n3).


# 04.3 (Wolf, goat, cabbage problem)
# A farmer with a wolf, a goat, and a cabbage must cross a river by boat. 
# The boat can carry only the farmer and one among the wolf, the goat, and the cabbage.
# If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage. 
# The farmer must help them all cross the river without anything being eaten. 
# Write a Bounded Model Checking procedure to find a successfull strategy for the farmer.

from utils import printModelBMC
from z3 import *


# Create a list of variables w_0, w_1, w_2 to represent the wolf at different states
w = [Int(f'w_{i}') for i in range(3)]

# Create a list of variables g_0, g_1, g_2 to to represent the goat at different states
g = [Int(f'g_{i}') for i in range(3)]

# Create a list of variables c_0, c_1, c_2 to to represent the cabbage at different states
c = [Int(f'c_{i}') for i in range(3)]


# A state should be an assimilation of the states of the wolf, goat & cabbage right?



# Create a datatype to represent the actions of choosing a wolf, goat or a cabbage
Function = Datatype('Actions')
Function.declare('Choose Wolf')
Function.declare('Choose Goat')
Function.declare('Choose Cabbage')
Function = Function.create()

# Create a list of variables to represent the function applied at each step
function = [Const("f_%s" % (i), Function) for i in range(3)]

# Python function that express the relation between the variables under an action
def Choose_Wolf(w_now):
    w_next = w_now
    return x_next == x_now + 17




# 04.4 (Tower of Hanoi)
# Write a Bounded Model Checking procedure to solve the Tower of Hanoi problem with n disks. Don't use any known algorith.
# https://en.wikipedia.org/wiki/Tower_of_Hanoi