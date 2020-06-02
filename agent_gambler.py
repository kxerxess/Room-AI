import numpy as np
import random


class Gambler:
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
        self.exploration_rate = 1.0
        self.learning_rate = 0.1
        self.discount = 0.95
        self.exploration_delta = 1/10000

    def get_next_action(self,state):
        if random.random() < self.exploration_rate:
            return self.random_action(state)
        else:
            return self.greedy_action(state)

    def greedy_action(self, state):
        self.curr_state_x = state[0]
        self.curr_state_y = state[1]
        self.q_values = [self.t_q_table[self.curr_state_x, self.curr_state_y],
                         self.b_q_table[self.curr_state_x, self.curr_state_y],
                         self.l_q_table[self.curr_state_x, self.curr_state_y],
                         self.r_q_table[self.curr_state_x, self.curr_state_y]]
        if len(set(self.q_values)) == len(self.q_values):
            return self.actions[self.q_values.index(max(self.q_values))]
        else:
            max_q = max(self.q_values)
            max_q_values_index = []
            for i in range(len(self.q_values)):
                if self.q_values[i] == max_q:
                    max_q_values_index.append(i)
            return self.actions[random.choice(max_q_values_index)]

    def random_action(self, state):
        return random.choice(self.actions)

    def update(self, old_state, action, reward, new_state):
        sxo = old_state[0]
        syo = old_state[1]
        sxn = new_state[0]
        syn = new_state[1]
        old_value = self.q_table[self.actions.index(action)][sxo, syo]
        future_action = self.greedy_action(new_state)
        future_reward = self.q_table[self.actions.index(future_action)][sxn][syn]
        new_value = old_value + self.learning_rate * (reward + self.discount * future_reward - old_value)
        self.q_table[self.actions.index(action)][sxo][syo] = new_value

        if self.exploration_rate > 0:
            self.exploration_rate -= self.exploration_delta



