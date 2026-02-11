
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


# Create a list of variables to represent the farmer at different states
N = 100
f = [Int(f'f_{i}') for i in range(N)]

# Create a list of variables to represent the wolf at different states
w = [Int(f'w_{i}') for i in range(N)]

# Create a list of variables to represent the goat at different states
g = [Int(f'g_{i}') for i in range(N)]

# Create a list of variables to represent the cabbage at different states
c = [Int(f'c_{i}') for i in range(N)]


# Create a datatype to represent the actions of choosing a wolf, goat or a cabbage
Function = Datatype('Actions')
Function.declare('GoAlone')
Function.declare('ChooseWolf')
Function.declare('ChooseGoat')
Function.declare('ChooseCabbage')
Function = Function.create()

# Create a list of variables to represent the function applied at each step
function = [Const("f_%s" % (i), Function) for i in range(N - 1)]


# Python function that express the relation between the variables under an action
def Go_Alone(f_now, f_next):
    return f_next == 1 - f_now

def Choose_Wolf(w_now, w_next):
    return w_next == 1 - w_now

def Choose_Goat(g_now, g_next):
    return g_next == 1 - g_now

def Choose_Cabbage(c_now, c_next):
    return c_next == 1 - c_now


# Define the initial state
initial_state = And(f[0]==0, w[0]==0, g[0]==0, c[0]==0)

# Create the solver
s = Solver()

# Add the initial state constraint
s.add(initial_state)

# Add additional constraints: each entity can be in bank 0 or bank 1
for i in range(N):
    s.add(Or(f[i]==0, f[i]==1))
    s.add(Or(w[i]==0, w[i]==1))
    s.add(Or(g[i]==0, g[i]==1))
    s.add(Or(c[i]==0, c[i]==1))


# Define property constraint of wolf eating goat
P1 = And([Implies(w[i] == g[i], f[i] == w[i]) for i in range(N)])

# Define property constraint of goat eating cabbage
P2 = And([Implies(g[i] == c[i], f[i] == g[i]) for i in range(N)])

s.add(P1, P2)


# Add the transition relation constraints
for i in range(N - 1):
    transition = Or(
        And(
            function[i] == Function.GoAlone,
            Go_Alone(f[i], f[i+1]),
            w[i+1] == w[i],
            g[i+1] == g[i],
            c[i+1] == c[i],
        ),
        And(
            function[i] == Function.ChooseWolf,
            f[i] == w[i],
            Go_Alone(f[i], f[i+1]),
            Choose_Wolf(w[i], w[i+1]),
            g[i+1] == g[i],
            c[i+1] == c[i],
        ),
        And(
            function[i] == Function.ChooseGoat,
            f[i] == g[i],
            Go_Alone(f[i], f[i+1]),
            Choose_Goat(g[i], g[i+1]),
            w[i+1] == w[i],
            c[i+1] == c[i],
        ),
        And(
            function[i] == Function.ChooseCabbage,
            f[i] == c[i],
            Go_Alone(f[i], f[i+1]),
            Choose_Cabbage(c[i], c[i+1]),
            w[i+1] == w[i],
            g[i+1] == g[i],
        )
    )
    s.add(transition)

# Goal: everyone on the right bank at some step
s.add(Or([And(f[i] == 1, w[i] == 1, g[i] == 1, c[i] == 1) for i in range(N)]))

if s.check() == sat:
    m = s.model()
    print("Found a safe plan:")

    counter = 0
    for i in range(N):
        if (m[f[i]] == 1 and m[w[i]] == 1 and m[g[i]] == 1 and m[c[i]] == 1):
            counter = i
            break

    if counter is not None:
        print(f"Reached goal at step {counter}")
        for i in range(counter + 1):
            action_val = m[function[i]] if i < N - 1 else None
            print(f"step {i}: f={m[f[i]]}, w={m[w[i]]}, g={m[g[i]]}, c={m[c[i]]}, action={action_val}")
else:
    print("No plan found within the bound.")


# 04.4 (Tower of Hanoi)
# Write a Bounded Model Checking procedure to solve the Tower of Hanoi problem with n disks. Don't use any known algorith.
# https://en.wikipedia.org/wiki/Tower_of_Hanoi