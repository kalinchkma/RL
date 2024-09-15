import numpy as np 
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, p):
        self.p = p # win rate of the bandit
        self.p_estimate = 0. # initial probability estimate of the bandit
        self.n = 0 # number of time has been played

    def pull(self):
        return np.random.random() < self.p

    def update(self, x):
        self.n += 1
        self.p_estimate = ((self.n - 1)*self.p_estimate + x) / self.n 

def ucb(mean, n, nj):
    return mean + np.sqrt(2*np.log(n)/nj)

def experiment(m1, m2, m3, num_trails):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]
    rewards = np.empty(num_trails)

    total_plays = 0

    # Play each bandit once
    for b in bandits:
        r = b.pull()
        total_plays += 1
        b.update(r)

    for i in range(num_trails):
        j = np.argmax([ucb(b.p_estimate, total_plays, b.n) for b in bandits])
        r = bandits[j].pull()

        # count total number has been played
        total_plays += 1

        # update rewards
        bandits[j].update(r)

        # collect rewards
        rewards[i] = r

    cumulative_average = np.cumsum(rewards) / (np.arange(num_trails) + 1)
    
    print("Total number played", total_plays)
    
    for b in bandits:
        print("true p:", b.p, " p estimate: ", b.p_estimate, " number of time played: ", b.n)

    # plt moving average 
    plt.plot(cumulative_average)
    plt.plot(np.ones(num_trails)*np.max([m1, m2, m3]))
    plt.xscale('log')
    plt.show()
    


if __name__ == "__main__":
    experiment(0.2, 0.5, 0.75, 10000)


