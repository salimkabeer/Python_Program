
def incr(x):
    return x + 1


def decr(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


if __name__ == '__main__':
    print("Increment 3 : ", operate(incr, 3))
    print("Decrement 6 : ", operate(decr, 6))
