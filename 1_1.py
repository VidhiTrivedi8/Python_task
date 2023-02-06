ones = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ]


def numtoword(n, suffix):
    if n > 19:
        str += tens[n / 10] + ones[n % 10]
    else:
        str += ones[n]
    if n:
        str += suffix
    return str


def convtowords(n):
    res = " "
    if n  in range(1001,100000):
    res += numtoword((n / 100000) % 100, "lakh")
    res += numtoword((n / 1000) % 100, "thousand")
    res += numtoword((n / 100) % 10, "hundred")
    res += numtoword((n % 100), " ")
    return res

#driver code
while True:
    num = int(input("Enter the number: "))
    s = convtowords(num)
    print(num, ":", s)

