def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# driver code
while True:
    num = int(input("Enter the integer"))
    if num != 0:
        print(num, "has", count_ones(num), "1's in its binary form")
    else:
        break
