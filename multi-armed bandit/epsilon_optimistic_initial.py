"""
Choosing the bandit
- Be greedy
- Choose the bandit arm with "largest estimated mean"
- Balance exploration (collect data) and exploitation
- Early in experiment:
    - Less data
    - Estimated mean is large (because initial value in large / optimistic)
- Later in experiment:
    - Lots of data collected
    - Estimated mean continues to get smaller until we stop choosing the 
      bandit or it converges
- Arithmetic average: even if initial value is very large, its effect disappears as
  more data collected
"""
import numpy as np
import matplotlib.pyplot as plt # type: ignore

class Bandit:
    def __init__(self, p) -> None:
        self.p = p
        self.p_estimate = 5.
        self.n = 1.
    
    def pull(self):
        return np.random.random() < self.p
    
    def update(self, x):
        self.n += 1
        self.p_estimate = ((self.n - 1) * self.p_estimate + x)/self.n

def experiment(m1, m2, m3, n):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

    rewards = np.zeros(n)

    for i in range(n):
        # pick the optimal bandits
        j = np.argmax([b.p_estimate for b in bandits])

        # pull the arm of the bandit 
        r = bandits[j].pull()

        # Collect the rewards
        rewards[i] = r

        # update the bandit
        bandits[j].update(r)
    
    print("Total reward collected:", rewards.sum())

    for b in bandits:
        print("Bandit probability: ", b.p, "estimate: ",b.p_estimate, "Number of time playerd: ", b.n)
    
    # plot the result
    cumsum_rewards = np.cumsum(rewards)
    win_rate = cumsum_rewards / (np.arange(n) + 1)
    plt.plot(win_rate)
    plt.plot(np.ones(n)*np.max([m1, m2, m3]))
    plt.show()


if __name__ == "__main__":
    experiment(0.2, .5, .75, 10000)


