import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import scipy


def brownian(init=100, steps=10000, mu=0, sigma=1):
    series = [init]
    for _ in range(1, steps + 1):
        previousStep = series[-1:][0]
        currentStep = previousStep + random.normalvariate(mu, sigma)
        series = series + [currentStep]
    return series


def geoBrownian(init=100, steps=100, mu=0, sigma=0.0025):
    series = [init]
    for _ in range(1, steps):
        normalOffset = random.normalvariate(mu, sigma)
        previousStep = series[-1:][0]
        currentStep = np.exp(np.log(previousStep) + normalOffset)
        series = series + [currentStep]
    return series


steps = 1000
x_points = range(1, steps + 1)

trials = 100


def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)


colors = get_cmap(trials)

# for i in range(trials):
#     plt.plot(x_points, geoBrownian(steps=steps), color=colors(i + 1))

# plt.show()


def extractSubsequences(
    series,
    windowSize=10,
    threshold=1,
):
    goodSubsequences = []
    for i in range(0, len(series) - windowSize + 1):
        window = series[i : windowSize + i]
        try:
            if series[windowSize + i] > threshold:
                goodSubsequences[i] = window
        except:
            break
    return goodSubsequences


i = 0
while i < len(extractSubsequences(geoBrownian(steps=steps))):
    break
    # pad the subsequences here
