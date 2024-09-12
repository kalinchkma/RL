import matplotlib.pyplot as plt # type: ignore
import numpy as np

class BanditArm:
    def __init__(self, p) -> None:
        self.p = p
        self.p_estimate = 0
        self.n = 0
    
    def pull(self):
        return np.random.randn() + self.p
    
    def update(self, x):
        self.n += 1
        self.p_estimate = (1-1.0/self.n)*self.p_estimate + 1.0/self.n*x

def experiment(m1, m2, m3, eps, N):
    bandits = [BanditArm(m1), BanditArm(m2), BanditArm(m3)]

    # count number of suboptimal choices
    means = np.array([m1, m2, m3])
    true_best = np.argmax(means)
    count_suboptimal = 0

    data = np.empty(N)

    for i in range(N):
        # epsilon greedy
        p = np.random.random()
        if p < eps:
            j = np.random.choice(len(bandits))
        else:
            j = np.argmax([b.p_estimate for b in bandits])
        
        x = bandits[j].pull()
        bandits[j].update(x)

        if j != true_best:
            count_suboptimal += 1
        
        # for the plot
        data[i] = x
    
    comulative_average = np.cumsum(data) / (np.arange(N) + 1)

    for b in bandits:
        print(b.p_estimate)

    print("percent suboptimal for epsilon = %s:" % eps, float(count_suboptimal)/N)

    # plot moving average ctr
    plt.plot(comulative_average)
    plt.plot(np.ones(N) * m1)
    plt.plot(np.ones(N) * m2)
    plt.plot(np.ones(N) * m3)
    plt.xscale("log")
    plt.show()


    return comulative_average

if __name__ == "__main__":
    m1, m2, m3 = 1.5, 2.5, 3.5
    e_1 = experiment(m1, m2, m3, 0.1, 1000)
    e_2 = experiment(m1, m2, m3, 0.05, 1000)
    e_3 = experiment(m1, m2, m3, 0.01, 1000)    

    # log scale plot
    plt.plot(e_1, label='eps = 0.1')
    plt.plot(e_2, label="eps = 0.05")
    plt.plot(e_3, label="eps = 0.01")
    plt.legend()
    plt.xscale('log')
    plt.show()
 
    
