import numpy as np


def easeInSine(x):
    return 1 - np.cos((x * np.pi) / 2)


def easeOutSine(x):
    return np.sin((x * np.pi) / 2)


def easeInOutSine(x):
    return -(np.cos(np.pi * x) - 1) / 2
