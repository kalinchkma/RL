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

NUM_TRAILS = 1000
EPS = 0.1
BANDIT_PROBABILITES = [0.2, 0.5, 0.75]


def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBABILITES]

    rewards = np.zeros(NUM_TRAILS)
    
    num_times_explored = 0
    num_times_exploited = 0
    num_optimal = 0
    optimal_bandit = np.argmax([b.p for b in bandits])
    print("optimal bandit:", optimal_bandit)

    for i in range(NUM_TRAILS):

        # use epsilon-greedy to select the next bandit
        if np.random.random() < EPS:
            num_times_explored += 1
            j = np.random.randint(len(bandits))
        else:
            num_times_exploited += 1
            j = np.argmax([b.p_estimate for b in bandits])

        if j == optimal_bandit:
            num_optimal += 1
        
        # pull the arm for the bandit with the largest smaple
        x = bandits[j].pull()
        print("x value:", x)

        # update the rewards log
        rewards[i] = x

        # update the distribution for the bandit whose arm we just pulled
        bandits[j].update(x)
    
    # print mean estmates for each bandit
    for b in bandits:
        print("mean estimate:", b.p_estimate)
    
    # print total reward
    print("total reward earned:", rewards.sum())
    print("overall win rate:", rewards.sum() / NUM_TRAILS)
    print("num_times_explored:", num_times_explored)
    print("num_times_exploited:", num_times_exploited)
    print("num times selected optimal bandit: ", num_optimal)

    # plot the results
    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRAILS) + 1)
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRAILS)*np.max(BANDIT_PROBABILITES))
    plt.show()
    for b in bandits:
        print(b.p, b.p_estimate, b.N)
    

if __name__ == "__main__":
    experiment()

