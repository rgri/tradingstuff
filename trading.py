import random
import matplotlib.pyplot as plt
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
y_points = geoBrownian(steps=steps)
x_points = range(1, steps + 1)

print(y_points)
plt.plot(x_points, y_points)
plt.show()
