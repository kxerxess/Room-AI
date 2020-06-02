import numpy as np
import tensorflow as tf
from keras.layers import Dense, Input
from keras.models import Sequential
from keras.optimizers import Adam
import random


class Pintu:
    def __init__(self):
        self.actions = ['T', 'B', 'L', 'R']
        self.curr_state_x = None
        self.curr_state_y = None
        self.action = None
        self.exploration_rate = 1.0
        self.lr = 0.1
        self.discount = 0.95
        self.exploration_delta = 1 / 10000
        self.input_size = 2
        self.model = self.build_dqn(self.lr, self.input_size, len(self.actions), 8, 8)

    def build_dqn(self, lr, input_size, nb_actions, fc1_dim, fc2_dim):
        self.lr = lr
        self.model = Sequential([
            Dense(fc1_dim, activation='relu', input_shape=(2,)),
            Dense(fc2_dim, activation='relu'),
            Dense(nb_actions, activation='sigmoid')
        ])
        self.model.compile(optimizer=Adam(learning_rate=self.lr), loss='mean_squared_error')
        return self.model

    def get_next_action(self, state):
        if random.random() < self.exploration_rate:
            return random.choice(self.actions)
        else:
            sx = state[0]
            sy = state[1]
            q_actions = self.model.predict(np.array([[sx, sy]]))
            action = np.argmax(q_actions)
            action = self.actions[int(action)]
            #print("Get Action:", action)
            return action

    def update(self, old_state, action, reward, new_state):
        sxo = old_state[0]
        syo = old_state[1]
        sxn = new_state[0]
        syn = new_state[1]
        old_q = self.model.predict(np.array([[sxo, syo]]))
        new_q = self.model.predict(np.array([[sxn, syn]]))
        #print(type(old_q), old_q)
        #print('Update Action:', action)
        old_q[0][self.actions.index(action)] = reward + self.discount * np.amax(new_q)
        self.model.train_on_batch(np.array([[sxo, syo]]), [old_q])

        if self.exploration_rate > 0:
            self.exploration_rate -= self.exploration_delta




