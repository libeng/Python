def easeOutBounce(x):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x ** 2
    elif x < 2 / d1:
        return n1 * (x - 1.5 / d1) ** 2 + 0.75
    elif x < 2.5 / d1:
        return n1 * (x - 2.25 / d1) ** 2 + 0.9375
    else:
        return n1 * (x - 2.625 / d1) ** 2 + 0.984375


def easeInBounce(x):
    return 1 - easeOutBounce(1 - x)


def easeInOutBounce(x):
    if x < 0.5:
        return (1 - easeOutBounce(1 - 2 * x)) / 2
    else:
        return (1 + easeOutBounce(2 * x - 1)) / 2
