import numpy as np


def logistic_model(x, a, b, c):
    return c / (1 + np.exp(-(x - b) / a))


def exponential_model(x, a, b, c):
    return a * np.exp(b * (x - c))
