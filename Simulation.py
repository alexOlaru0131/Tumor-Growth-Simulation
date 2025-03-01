import multiprocessing
import numpy as np
from Tumor import TumorEnv

def trainAgent(envId):
    env = TumorEnv()
    for _ in range(10):
        state = env.reset()
        done = False
        while not done:
            action = np.random.choice([0, 1, 2])
            # state, reward, done, _ = env.step(action)
            env.render()

def runParallelSimulations(n):
    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=trainAgent, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()