import comp_str

str1 = input("Enter the 1st string\n")
str2 = input("Enter the 2nd string\n")

ch = comp_str.func(str1, str2)

if ch == 0:
    print("Strings are equal")
else:
    print("Strings are not equal")
