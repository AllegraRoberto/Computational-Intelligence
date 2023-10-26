from random import random
from functools import reduce
from collections import namedtuple, deque
from queue import PriorityQueue
import numpy as np
from tqdm.auto import tqdm

PROBLEM_SIZE = 100
NUM_SETS = 200
SETS = tuple(np.array([random() < 0.2 for _ in range(PROBLEM_SIZE)]) for _ in range(NUM_SETS))

for x in SETS:
    print(x)

State = namedtuple('State', ['taken', 'not_taken'])

def covered(state):
    return reduce(
        np.logical_or,
        [SETS[i] for i in state.taken],
        np.array([False for _ in range(PROBLEM_SIZE)]),
    )

def goal_check(state):
    return np.all(covered(state))

assert goal_check(State(set(range(NUM_SETS)), set())), "Probelm not solvable"

def h(state):
    return PROBLEM_SIZE - sum(covered(state))

def f(state):
    return len(state.taken) + h(state)

frontier = PriorityQueue()
state = State(set(), set(range(NUM_SETS)))
frontier.put((f(state), state))

counter = 0
_, current_state = frontier.get()
with tqdm(total=None) as pbar:
    while not goal_check(current_state):
        counter += 1
        for action in current_state[1]:
            new_state = State(
                current_state.taken ^ {action},
                current_state.not_taken ^ {action},
            )
            frontier.put((f(new_state), new_state))
        _, current_state = frontier.get()
        pbar.update(1)

print(f"Solved in {counter:,} steps ({len(current_state.taken)} tiles)")
