def func(x, y):
    ch = 0
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                ch = -abs(1)
                break
            else:
                ch = 0
    return ch
