def easeInQuint(x):
    return x ** 5


def easeOutQuint(x):
    return 1 - (1 - x) ** 5


def easeInOutQuint(x):
    if x < 0.5:
        return 16 * x ** 5
    else:
        return 1 - (-2 * x + 2) ** 5 * 0.5
