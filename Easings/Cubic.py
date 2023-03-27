def easeInCubic(x):
    return x ** 3


def easeOutCubic(x):
    return 1 - (1 - x) ** 3


def easeInOutCubic(x):
    if x < 0.5:
        return 4 * x ** 3
    else:
        return 1 - (-2 * x + 2) ** 3 / 2
