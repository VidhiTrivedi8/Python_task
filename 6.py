def checkfirst(l1):
    i = ord(l1[0])
    # print(i)
    if i != 45:
        printing(l1)
    else:
        l1.remove(l1[0])
        checkfirst(l1)


def printing(l1):
    x = ord(l1[0])
    y = ord(l1[-1])
    res = ""
    for i in range(x, y+1):
        res = res + chr(i)
    ex = str(res)
    print(ex)


# driver code
string = input("Enter the string:")
l1 = []
# ll1 = []
l1[:0] = string
checkfirst(l1)
