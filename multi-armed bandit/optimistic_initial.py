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
class Bandit:
    def __init__(self, p) -> None:
        self.p = p
        self.p_estimate = 5.
        self.n = 1.


