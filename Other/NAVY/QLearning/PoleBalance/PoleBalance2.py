



from collections import deque

import gym
import numpy as np


class PoleBalance:
    def __init__(self):
        no_buckets = (1, 1, 6, 3)
        no_actions = 2
        self.q_value_table = np.zeros(no_buckets + (no_actions,))
        print(self.q_value_table)

        self.env = gym.make('CartPole-v0')
        print(self.env.action_space.n)
        self.agent_memory = np.full((1000, 1000), 0)
        print(self.agent_memory)
        pass

    def choose_action(self, state):
        return self.env.action_space.sample()

    def bucketize_state_value(state_value):
        bucket_indexes = []
        for i in range(len(state_value)):
            if state_value[i] <= state_value_bounds[i][0]:
                bucket_index = 0
            elif state_value[i] >= state_value_bounds[i][1]:
                bucket_index = no_buckets[i] - 1
            else:
                bound_width = state_value_bounds[i][1] - state_value_bounds[i][0]
                offset = (no_buckets[i] - 1) * state_value_bounds[i][0] / bound_width
                scaling = (no_buckets[i] - 1) / bound_width
                bucket_index = int(round(scaling * state_value[i] - offset))
                bucket_indexes.append(bucket_index)
        return tuple(bucket_indexes)

    def remember(self, state, action, reward, next_state, done):
        print((state, action, reward, next_state, done))
        # self.agent_memory.append((state, action, reward, next_state, done))

    def train(self, iteration_count: int = 100, learning_rate: float = 0.8):
        for i in range(1):
            state = self.env.reset()
            done = False
            score = 0
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                self.remember(state, action, reward, next_state, done)
                self.env.l_system_render()
                state = next_state
                score += 1
                # self.agent_memory = score + learning_rate * max()
                print(state)

    def test(self):
        pass
