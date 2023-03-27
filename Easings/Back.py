def easeInBack(x):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * x ** 3 - c1 * x ** 2


def easeOutBack(x):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def easeInOutBack(x):
    c1 = 1.70158
    c2 = c1 * 1.525
    if x < 0.5:
        return (2 * x) ** 2 * ((c2 + 1) * 2 * x - c2) / 2
    else:
        return ((2 * x - 2) ** 2 * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2
