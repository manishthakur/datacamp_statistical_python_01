#
# If you have a story, you can simulate it!
# Sometimes, the story describing our probability distribution does not have a named distribution to go along with it. In these cases, fear not! You can always simulate it. We'll do that in this and the next exercise.
#
# In earlier exercises, we looked at the rare event of no-hitters in Major League Baseball. Hitting the cycle, when a batter gets all four kinds of hits in a single game, is another rare baseball event. Like no-hitters, this can be modeled as a Poisson process, so the time between hits of the cycle are also Exponentially distributed.
#
# How long must we wait to see a no-hitter and then a batter hit the cycle? The idea is that we have to wait some time for the no-hitter, and then after the no-hitter, we have to wait for hitting the cycle. Stated another way, what is the total waiting time for the arrival of two different Poisson processes in succession? The total waiting time is the time waited for the no-hitter, plus the time waited for the hitting the cycle.
#
# Now, you will write a function to sample out of the distribution described by this story.
#
# Define a function with call signature successive_poisson(tau1, tau2, size=1) that samples the waiting time for a no-hitter and a hit of the cycle.
# Draw waiting times (size number of samples) for the no-hitter out of an exponential distribution parametrized by tau1 and assign to t1.
# Draw waiting times (size number of samples) for hitting the cycle out of an exponential distribution parametrized by tau2 and assign to t2.
# The function returns the sum of the waiting times for the two events.

import numpy as np
import matplotlib.pyplot as plt


# Compute mean and standard deviation: mu, sigma
def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = rng.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = rng.exponential(tau2, size)

    return t1 + t2
