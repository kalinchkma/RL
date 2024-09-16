import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, p):
        self.p = p
        self.p_estimate = 0.
        self.n = 0

    def pull(self):
        return np.random.random() < self.p

    def update(self, x):
        pass

