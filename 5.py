def search(ar, num, se):
    if se in num:
        ind = num.index(se)
    else:
        ind = -abs(1)
    return ind


# driver code

while True:

    a = int(input("Number of elements in the array:-"))
    if a == 0:
        break
    else:
        n = list(map(int, input("elements of array:-").strip().split()))
        ser = int(input("Enter the number you want to search:"))
        inde = search(a, n, ser)

        if inde >= 0:
            print("Number found whose index is : ", inde)
        else:
            print("String Not found", inde)
