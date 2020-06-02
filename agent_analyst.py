import random
import numpy as np


class Analyst:
    def __init__(self):
        self.t_q_table = np.zeros((5, 5), dtype=int)
        self.b_q_table = np.zeros((5, 5), dtype=int)
        self.l_q_table = np.zeros((5, 5), dtype=int)
        self.r_q_table = np.zeros((5, 5), dtype=int)
        self.q_table = [self.t_q_table, self.b_q_table, self.l_q_table, self.r_q_table]
        self.actions = ['T', 'B', 'L', 'R']
        self.q_values = []
        self.curr_state_x = None
        self.curr_state_y = None
        self.action = None

    def get_next_action(self, state):
        self.curr_state_x = state[0]
        self.curr_state_y = state[1]
        self.q_values = [self.t_q_table[self.curr_state_x, self.curr_state_y], self.b_q_table[self.curr_state_x, self.curr_state_y], self.l_q_table[self.curr_state_x, self.curr_state_y], self.r_q_table[self.curr_state_x, self.curr_state_y]]
        if len(set(self.q_values)) == len(self.q_values):
            return self.actions[self.q_values.index(max(self.q_values))]
        else:
            max_q = max(self.q_values)
            max_q_values_index = []
            for i in range(len(self.q_values)):
                if self.q_values[i] == max_q:
                    max_q_values_index.append(i)
            return self.actions[random.choice(max_q_values_index)]

    def update(self, old_state, action, reward, new_state):
        sx = old_state[0]
        sy = old_state[1]
        if action == 'T':
            self.t_q_table[sx, sy] += reward
        elif action == 'B':
            self.b_q_table[sx, sy] += reward
        elif action == 'L':
            self.l_q_table[sx, sy] += reward
        elif action == 'R':
            self.r_q_table[sx, sy] += reward



