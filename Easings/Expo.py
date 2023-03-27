def easeInExpo(x):
    if x == 0:
        return x
    else:
        return 2 ** (10 * x - 10)


def easeOutExpo(x):
    if x == 1:
        return x
    else:
        return 1 - 2 ** (-10 * x)


def easeInOutExpo(x):
    if x == 0 or x == 1:
        return x
    elif x < 0.5:
        return 2 ** (20 * x - 10) * 0.5
    else:
        return (2 - 2 ** (-20 * x + 10)) * 0.5
