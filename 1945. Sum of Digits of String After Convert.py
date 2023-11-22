def getLucky(s, k):
    allnum = ''
    for c in s:
        asc = ord(c)
        inte = int(asc) - 96
        allnum += str(inte)
        temp = [int(i) for i in allnum]


    print(temp)
    result =0
    for m in range(k):
        result = 0
        for n in temp:
            result +=n
            print(result)
        temp = [int(i) for i in str(result)]
        
        print(temp)
    return result

s = 'leetcode'

print(getLucky(s,2))
