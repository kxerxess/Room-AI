import random
from random import randint as rint


class RandomAF:
    def __init__(self):
        self.q_table = None
        self.actions = ['T', 'B', 'L', 'R']

    def get_next_action(self, state):
        return self.actions[rint(0, 3)]

    def update(self, old_state, action, reward, new_state):
        pass
