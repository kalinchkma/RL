# Multi-armed Bandit

### Probability:

- What kind of distributions are these?
    - P(A,B)
    - P(A|B)
- Answer:
    - P(A,B) -> Joint distribution
        - Read: 
        
    - P(A|B) -> Conditional distribution
        - Read: P of A given B

- Question:
    - Given:
        - p(x,y)
    - Want to find:
        - p(y)
    - What is this process called? What do we call p(y) in this content?
    - How do we do it?
- Answer:
    - This is called **marginalization**, and p(y) is called the **marginal** distribution
    - p(y) = sum(x)[x, y] -> Discrete x
    - p(y) = intergral(p(x, y))dx -> Continuous x
