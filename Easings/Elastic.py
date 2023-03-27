import numpy as np


def easeInElastic(x):
    c4 = 2 * np.pi / 3

    if x == 0 or x == 1:
        return x
    else:
        return -2 ** (10 * x - 10) * np.sin((x * 10 - 10.75) * c4)


def easeOutElastic(x):
    c4 = 2 * np.pi / 3
    if x == 0 or x == 1:
        return x
    else:
        return 2 ** (-10 * x) * np.sin((x * 10 - 0.75) * c4) + 1


def easeInOutElastic(x):
    c5 = (2 * np.pi) / 4.5

    if x == 0 or x == 1:
        return x
    elif x < 0.5:
        return -(2 ** (20 * x - 10) * np.sin((20 * x - 11.125) * c5)) * 0.5
    else:
        return (2 ** (-20 * x + 10) * np.sin((20 * x - 11.125) * c5)) * 0.5 + 1
