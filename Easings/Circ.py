def easeInCirc(x):
    return 1 - (1 - x ** 2) ** 0.5


def easeOutCirc(x):
    return (1 - (x - 1) ** 2) ** 0.5


def easeInOutCirc(x):
    if x < 0.5:
        return (1 - (1 - (2 * x) ** 2) ** 0.5) * 0.5
    else:
        return 0.5 * ((1 - (-2 * x + 2) ** 2) ** 0.5 + 1)
