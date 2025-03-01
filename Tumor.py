import numpy as np
import gym
import matplotlib.pyplot as plt
from gym import spaces

class TumorEnv(gym.Env):
    def __init__(self):
        super(TumorEnv, self).__init__()
        self.geneticCode = self.generateGeneticCode()
        self.spheres = [(np.array([0.0, 0.0, 0.0]), 0.0)]
        self.bloodVessels = []
        self.organ = self.generateOrgan()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=10, shape=(len(self.spheres), 3), dtype=np.float32)

    def generateGeneticCode(self, length=30):
        code = np.random.randint(0, 3, length)
        self.geneticTraits = {
            "density": sum(code[:5]) / 5,
            "growthRate": sum(code[5:10]) / 5,
            "asymmetry": sum(code[10:15]) / 5,
            "heterogeneity": sum(code[15:20]) / 5,
            "tissueType": sum(code[20:25]) % 3
        }
        return code

    def generateOrgan(self):
        return np.array([0.0, 0.0, -5.0]), 10.0

    def step(self, action):
        growthFactor = self.geneticTraits["growthRate"]
        newSpheres = int(growthFactor * (2.0 if action == 1 else (0.5 if action == 2 else 1.0)))

        for _ in range(newSpheres):
            parent = self.spheres[np.random.randint(len(self.spheres))]
            direction = np.random.randn(3) * 0.4
            direction /= np.linalg.norm(direction)
            newCenter = parent[0] + direction * 1.1
            newRadius = np.clip(np.random.normal(1.0, 0.2), 0.8, 1.2)
            self.spheres.append((newCenter, newRadius))

        if len(self.spheres) % 10 == 0:
            newVesselStart = np.random.rand(3) * 10 - 5
            newVesselEnd = self.spheres[-1][0]
            self.bloodVessels.append((newVesselStart, newVesselEnd))

        reward = len(self.spheres) * 0.1
        done = len(self.spheres) > 200
        return np.array([s[0] for s in self.spheres]), reward, done, {}

    def reset(self):
        self.spheres = [(np.array([0.0, 0.0, 0.0]), 0.0)]
        self.bloodVessels = []
        return np.array([s[0] for s in self.spheres])

    def render(self):
        organCenter, organRadius = self.organ
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        tissueColors = [(0.8, 0.4, 0.4), (0.6, 0.6, 0.8), (0.9, 0.6, 0.4)]
        color = tissueColors[self.geneticTraits["tissueType"]]
        for center, radius in self.spheres:
            u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
            x = radius * np.cos(u) * np.sin(v) + center[0]
            y = radius * np.sin(u) * np.sin(v) + center[1]
            z = radius * np.cos(v) + center[2]
            ax.plot_surface(x, y, z, color=color, alpha=0.6)

        for start, end in self.bloodVessels:
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color='red', linewidth=2)

        u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
        x = organRadius * np.cos(u) * np.sin(v) + organCenter[0]
        y = organRadius * np.sin(u) * np.sin(v) + organCenter[1]
        z = organRadius * np.cos(v) + organCenter[2]
        ax.plot_surface(x, y, z, color=(0.9, 0.6, 0.3), alpha=0.3)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()