# Bayesian Bandits / Thompson Smapling

- When dataset is small confidence interval is **large**, when dataset is big confidence interval is **small**
- when confidence interval large(Fat) -> Explore more, If Skinny -> Explore less, exploit more

## Bayes Rule

- p(θ | X) = (p(X | θ)*p(θ))/p(X) 
    - where θ is the mean of barnoulli random variable X, 
    - X is the data we have collected
    - p(θ) is called **Prior**
    - p(X) is called **Evidence**
    - p(X | θ) is Likelihood

## Update Bayes Rule equation
- p(θ | X) <+> p(X | θ)*p(θ) ['<+>' is posotional]
- Because in mathematics denominator is usually an impossible-to-slove integral

### Conjugate Priors
- There are special pairs of distributions where we can ignore the evidence and the  posterior has the same form as the prior
- In probability, we stick to a fixed set of distributions: Gaussian, Bernoulli, Binomial, Poisson etc.
- Conjugate priors are special: if we pick the right Likelihood and prior, the posterior will be the same kind of distributions as prior!

### Picking the bandit
- Instead of upper bound, use a sample drawn from posterior
- Instead of picking one value, we can make use of all possible values under the distributions(which will get skinner over time)
