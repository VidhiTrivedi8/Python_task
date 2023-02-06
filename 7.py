while True:

    str = input("Enter the string : ")

    if str == "exit":
        break
    else:

        count = 0

        for i in str:
            count = count + 1

        print("length of String:", count)
