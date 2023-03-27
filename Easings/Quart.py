def easeInQuart(x):
    return x ** 4


def easeOutQuart(x):
    return 1 - (1 - x) ** 4


def easeInOutQuart(x):
    if x < 0.5:
        return 8 * x ** 4
    else:
        return 1 - (-2 * x + 2) ** 4 * 0.5
