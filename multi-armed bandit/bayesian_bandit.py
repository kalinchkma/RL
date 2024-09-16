import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

class Bandit:
    def __init__(self, p):
        self.p = p
        self.a = 1
        self.b = 1
        self.n = 0

    def pull(self):
        return np.random.random() < self.p

    def update(self, x):
        self.n += 1
        self.b += 1 - x
        self.a += x

    def smaple(self):
        return np.random.beta(self.a, self.b)


def plot(bandits, trail):
    x = np.linspace(0, 1, 200)
    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        plt.plot(x, y, label=f"real p: {b.p:.4f}, win rate = {b.a -1}/{b.n}")
    plt.title(f"Bandit distributions after {trail} trails")
    plt.legend()
    plt.show()

def experiment():

    NUM_TRIALS = 2000
    BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]
    
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]
    
    sample_points = [5, 10, 20, 50, 100, 200, 500, 1000, 1500, 1999]
    rewards = np.zeros(NUM_TRIALS)
    for i in range(NUM_TRIALS):
        # Thompson sampling
        j = np.argmax([b.smaple() for b in bandits])
        
        # plot the posteriors
        if i in sample_points:
            plot(bandits, i)

        # pull the arm for the bandit with the largest sample
        x = bandits[j].pull()

        # update rewards
        rewards[i] = x

        # update the distributions for the  bandit whose arm we just pulled
        bandits[j].update(x)

    # print total rewards
    print("Total reward earned:", rewards.sum())
    print("overall win rate: ", rewards.sum() / NUM_TRIALS)
    print("num time selected each bandit:", [b.n for b in bandits])


if __name__ == "__main__":
    experiment()



    

