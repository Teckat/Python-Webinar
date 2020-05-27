i = 0
print(i)


def test():
    global i
    i = i+1
    print(i)


test()
print(i)
