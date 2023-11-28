def areOccurrencesEqual(s):
    counted =[]
    finalarr = []

    for i in range(len(s)):
        if s[i] not in counted:
            counted.append(s[i])
            count =1
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    count +=1
            finalarr.append(count)

        else:
            continue
    
    print(finalarr)
    for l in range(len(finalarr)):
        for m in range(l+1,len(finalarr)):
            if finalarr[l] != finalarr[m]:
                return False
        


    return True


s = 'aaabb'

print(areOccurrencesEqual(s))