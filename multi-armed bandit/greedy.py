import matplotlib.pyplot as plt # type: ignore
import numpy as np

class Bandit:
    def __init__(self, p) -> None:
        self.p = p # win rate of bandit
        self.p_estimate = 0.
        self.N = 0. # number of sample collected so far

    def pull(self):
        # draw a 1 with probability p
        return np.random.random() < self.p
    
    def update(self, x):
        self.N += 1
        self.p_estimate = ((self.N -1) * self.p_estimate + x)/self.N
