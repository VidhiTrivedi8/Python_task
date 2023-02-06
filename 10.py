def check(string, sub_str):
    if string.find(sub_str) == -1:
        print("Search Unsuccessful")
    else:
        print("Search Successful")


# driver code
a = 1
while a == 1:
    string = input("Enter the string: ")

    if string == "exit":
        print("exiting...")
        break

    sub_str = input("Enter the substring: ")
    check(string, sub_str)
