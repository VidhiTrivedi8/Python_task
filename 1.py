def int_to_word(n):
    ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ",
            "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
            "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + ones[n % 10]
    if n < 1000:
        return ones[n // 100] + "hundred " + int_to_word(n % 100)
    if n < 100000:
        return int_to_word(n // 1000) + "thousand " + int_to_word(n % 1000)
    if n < 1000000:
        return int_to_word(n // 100000) + "lakh " + int_to_word(n % 100000)


# driver code
while True:
    number = int(input("Enter a number"))
    if number in range(100000):
        if number == 0:
            print(number, ": zero")
        else:
            print(number, ":", int_to_word(number))
    else:
        break
