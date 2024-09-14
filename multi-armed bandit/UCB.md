# UCB

- UCB = Upper Confidence Bound
- In greedy
  - Epsilon-greedy - small probability of random (uniform) exploration
  - Optimistic - more naturally start at large value and fall into true mean
- In UCB, UCB use probability to get upper bound
  
## Applying Probability
- p(sample_mean - true_mean >= error) <= f(error) -> decreasing function
  - p(sample_mean - true_mean >= t) <= 1/t
- p(Xn - E(X) >= t) <= e^(-2nt^2)
  - Xn - smaple mean after collecting n samples
  - E(X) - expected value of X (true mean)
  - Xn - E(X) - measurement error of sample mean
  - t - arbitrary error value

## Actual Inequalitities
- Markov inequality: RHS decreases propotional to 1/t
- Chebyshev inequality: RHS decreases propotional to 1/t^2
  - This is tighter bound
- Hoeffding's inequality (even tighter)

## Pseudocode

Loop:
    j = argmax(Xnj + sqrt(2*(logN/nj)))
    # pull arm of j, update bandit j's mean ..