def invert_bits(n, start, count):
    # Create a mask with count number of 1's
    mask = (1 << count) - 1
    # Shift the mask to the starting position
    mask = mask << (start - count)
    # Invert the bits by XORing with the mask
    n = n ^ mask
    return n


# driver code
num = int(input("Enter the integer"))
print("Binary form of", num, "is", bin(num)[2:])
start = int(input("Enter the position from where you want to start the inversion"))
invnum = int(input("Enter the number of bits whose inversion should be done"))
inverted_num = invert_bits(num, start, invnum)
print("ans :", inverted_num,bin(inverted_num)[2:])
