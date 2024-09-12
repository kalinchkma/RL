import numpy as np


class Bandit:
    def __init__(self, p) -> None:
        self.p = p # default probability
        self.p_estimate = 0 # probability estimate
        self.n = 0 # number of time selected to play
    
    def pull(self):
        return np.random.random() < self.p

    def update(self, x):
        self.n += 1
        self.p_estimate = ((self.n - 1)*self.p_estimate + x)/self.n

NUM_TRAILS = 1000
BANDITS = [0.4, 0.9, 0.7]

def experiment():
    bandits = [Bandit(p) for p in BANDITS]

    rewards = np.zeros(NUM_TRAILS)

    optimal_bandit = np.argmax([b.p for b in bandits])
    print("optimal bandit index: ", optimal_bandit)

    for i in range(NUM_TRAILS):
        j = np.argmax([b.p for b in bandits])

        # pull the arm of bandit
        x = bandits[j].pull()

        # collect the rewards
        rewards[j] = x

        # update the bandit 
        bandits[j].update(x)
    
    print("Total reward earnd", rewards.sum())
    print("Win rate: ", rewards.sum()/NUM_TRAILS)

    # badit that has beed used to play
    for b in bandits:
        print(b.n, b.p, b.p_estimate)



if __name__ == "__main__":
    experiment()    
     

