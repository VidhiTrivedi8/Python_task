# dict
names = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
         10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
         17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
         60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand", }


def getwords(number):
    num = str(number)
    num = num.zfill(4)
    th = int(num[0])
    h = int(num[1])
    t = int(num[2])
    o = int(num[3])

    if th == 0:
        if h == 0:
            td, od = twodigit(t, o)
            print(number, ":", td, " ", od)
        elif t == 0:
            hd, od = threedigitz(h, o)
            print(number, ":", hd, " ", names.get(100), " ", od)
        else:
            n = int(num)
            hd = names.get(h)
            sd = threedigit(n)
            if sd != " ":
                print(number, ":", hd, " ", names.get(100), " ", sd)
            else:
                sd, td = twodigit(t, o)
                print(number, ":", hd, " ", names.get(100), " ", sd, " ", td)
    else:
        thd = names.get(th)
        n = int(num)
        if h == 0:
            if t == 0:
                od = names.get(o)
                print(number, ":", thd, " ", names.get(1000), " ", od)
            else:
                sd = threedigit(n)
                if sd != " ":
                    print(number, ":", thd, " ", names.get(1000), " ", sd)
                else:
                    sd, td = twodigit(t, o)
                    print(number, ":", thd, " ", names.get(1000), " ", sd, " ", td)
        else:
            hd = names.get(h)
            td, od = twodigit(n, t, o)
            if od != " ":
                print(number, ":", thd, " ", names.get(1000), " ", hd, " ", names.get(100), " ", td, " ", od)
            else:
                print(number, ":", thd, " ", names.get(1000), " ", hd, " ", names.get(100), " ", td)


def twodigit(n, t, o):
    c = n % 1000
    x = c % 100
    if x in names:
        td = names.get(x)
        od = " "
        return td, od
    else:
        tn = t * 10
        td = names.get(tn)
        od = names.get(o)
        return td, od


def threedigitz(h, o):
    hd = names.get(h)
    od = names.get(o)
    return hd, od


def threedigit(n):
    c = n % 100
    if c in names:
        sd = names.get(c)
        return sd
    else:
        return " "


# driver code
while True:
    number = int(input("Enter any number"))

    if number in names:
        k = names.get(number)
        print(number, ":", k)
    else:
        if len(str(number)) in range(2, 5):
            getwords(number)
        else:
            break
