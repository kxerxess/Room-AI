import numpy as np
import random
from random import randint as rint


class Room():
    def __init__(self):
        self.room_size = 5
        self.room = np.zeros((self.room_size, self.room_size), dtype=int)
        self.slip = 0.1
        self.large = 10
        self.small = -5
        self.state_x = 2
        self.state_y = 2
        self.state = [self.state_x, self.state_y]
        self.actions = ['T', 'B', 'L', 'R']
        self.reward = 0

    def take_action(self, action):
        self.reward = 0
        if random.random() < self.slip:
            action = self.actions[rint(0, 3)]
        if action == 'T':
            if self.state_x > 0:
                self.state_x -= 1
                self.state = [self.state_x, self.state_y]

        if action == 'B':
            if self.state_x < self.room_size-1:
                self.state_x += 1
                self.state = [self.state_x, self.state_y]

        if action == 'R':
            if self.state_y < self.room_size-1:
                self.state_y += 1
                self.state = [self.state_x, self.state_y]

        if action == 'L':
            if self.state_y > 0:
                self.state_y -= 1
                self.state = [self.state_x, self.state_y]

        if self.state == [0, 0] or self.state == [4, 4]:
            self.reward = self.large
        if self.state == [0, 4] or self.state == [4, 0]:
            self.reward = self.small

        return self.state, self.reward

    def reset(self):
        self.state = [2, 2]
