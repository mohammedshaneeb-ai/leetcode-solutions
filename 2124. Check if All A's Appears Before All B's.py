def checkString(s):
    flag = 0
    for i in range(len(s)):
        if s[i] == 'a':
            if flag == 1:
                return False
            else:
                continue
        elif s[i] == 'b':
            flag = 1
    return True          


s = "aaabbb"
print(checkString(s))