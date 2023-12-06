def prefixCount(words,pref):
    count = 0
    prelen = len(pref)
    for i in range(len(words)):
        if words[i][:prelen] == pref:
            count +=1
        else:
            continue
    return count


words = ["pay","attention","practice","attend"]
pref = "at"
print(prefixCount(words,pref))