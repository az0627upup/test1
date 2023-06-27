def check(str):
    flag = False
    a = [c.isupper() for c in str]
    b = [c.islower() for c in str]
    d = [c.isdigit() for c in str]
    test = "&*#^%!?"
    for i in range(len(test)):
        if test[i] in str:
            flag = True
    if sum(a)!=0 and sum(b)!=0 and sum(d)!=0 and flag == True:
        return True
    else:
        return False


if __name__ == '__main__':
    str = input()
    c = check(str)
    if c == True:
        print("OK")
    else:
        print("wrong")


