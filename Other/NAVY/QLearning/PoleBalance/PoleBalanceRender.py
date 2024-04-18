import gym

class PoleBalanceRender:
    def __init__(self):
        env = gym.make('CartPole-v1')
        state = env.reset()
        print(state)
        while True:
            action = env.action_space.sample()
            print(action)
            observation, reward, done, info = env.step(action)
            env.l_system_render()
            print(observation)
            print(reward)
            print(done)
            print(info)
            print()
            if done:
                break
        env.close()
