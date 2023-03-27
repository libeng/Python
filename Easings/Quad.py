def easeInQuad(x):
    return x ** 2


def easeOutQuad(x):
    return 1 - (1 - x) ** 2


def easeInOutQuad(x):
    if x < 0.5:
        return 2 * x ** 2
    else:
        return 1 - (-2 * x + 2) ** 2 * 0.5
