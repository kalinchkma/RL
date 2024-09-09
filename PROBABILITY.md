### Quick Probability:

- Question: What kind of distributions are these?
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

- Question: How do I calculate
    - E(X|Y)
- Answer:
  - This is the conditional expectation
    - E(X|Y) = integral(xp(x|y))dx -> Continuous x
    - E(X|Y) = sum(x)[xp(x|y)] -> Discrite x
- Question:
  - Expected value of a function
    - E[g(X)]
- Answer:
  - Expected value of a function
  - E(X) is a special case of this where the function is identity
  - E[g(X)] = sum(x)[g(x)p(x)] -> discrete x
  - E[g(X)] = integral(g(x)p(x))dx -> continous x
- Question:
  - Note: c is a constant, X and Y are random variables
  - Can we expand this expression?
    - Using the fect that expectation is a linear operator
    - E(cX + Y) = ?
- Answer:
  - E(cX + Y) = cE(X) + E(Y)

- Question:
  - What is that name of expected value `E(X)` ?
- Answer:
  - The Expected value also called a **mean** of **x**

