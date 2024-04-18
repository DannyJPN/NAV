import math
import random
from collections import deque

import gym
import numpy as np


class PoleBalance:
    environment = gym.make('CartPole-v0')

    no_buckets = (1, 1, 6, 3)
    no_actions = 2

    min_explore_rate = 0.01
    min_learning_rate = 0.1

    max_episodes = 1000
    max_time_steps = 250
    streak_to_end = 120
    solved_time = 199
    discount = 0.99
    no_streaks = 0

    state_value_bounds = list(zip(environment.observation_space.low,
                                  environment.observation_space.high))
    state_value_bounds[1] = [-0.5, 0.5]
    state_value_bounds[3] = [-math.radians(50), math.radians(50)]

    def __init__(self):

        self.agent_memory = np.zeros(self.no_buckets + (self.no_actions,))

    def select_action(self, state_value, explore_rate):
        if random.random() < explore_rate:
            action = self.environment.action_space.sample()
        else:
            action = np.argmax(self.agent_memory[state_value])
        return action

    def bucketize_state_value(self, state_value):
        bucket_indexes = []
        for i in range(len(state_value)):
            if state_value[i] <= self.state_value_bounds[i][0]:
                bucket_index = 0
            elif state_value[i] >= self.state_value_bounds[i][1]:
                bucket_index = self.no_buckets[i] - 1
            else:
                bound_width = self.state_value_bounds[i][1] - self.state_value_bounds[i][0]
                offset = (self.no_buckets[i] - 1) * self.state_value_bounds[i][0] / bound_width
                scaling = (self.no_buckets[i] - 1) / bound_width
                bucket_index = int(round(scaling * state_value[i] - offset))
            bucket_indexes.append(bucket_index)
        return tuple(bucket_indexes)


    def train(self):
        for episode_no in range(self.max_episodes):
            explore_rate = 0.5
            learning_rate = 0.5

            observation = self.environment.reset()

            start_state_value = self.bucketize_state_value(observation)
            previous_state_value = start_state_value

            for time_step in range(self.max_time_steps):
                self.environment.l_system_render()
                selected_action = self.select_action(previous_state_value, explore_rate)
                observation, reward_gain, completed, _ = self.environment.step(selected_action)
                state_value = self.bucketize_state_value(observation)
                best_q_value = np.amax(self.agent_memory[state_value])
                self.agent_memory[previous_state_value + (selected_action,)] += learning_rate * (
                        reward_gain + self.discount * (best_q_value) - self.agent_memory[previous_state_value + (selected_action,)])

                print('Episode number : %d' % episode_no)
                print('Time step : %d' % time_step)
                print('Selection action : %d' % selected_action)
                print('Current state : %s' % str(state_value))
                print('Reward obtained : %f' % reward_gain)
                print('Best Q value : %f' % best_q_value)
                print('Learning rate : %f' % learning_rate)
                print('Explore rate : %f' % explore_rate)
                print('Streak number : %d' % self.no_streaks)

                if completed:
                    print('Episode %d finished after %f time steps' % (episode_no, time_step))
                if time_step >= self.solved_time:
                    self.no_streaks += 1
                else:
                    self.no_streaks = 0
                    break
                previous_state_value = state_value
                if self.no_streaks > self.streak_to_end:
                    break

