def addbinary(a,b):
    carry = 0
    result = ''
    answer = 0
    i = len(a)-1

    la = len(a)
    lb = len(b)
    

    if len(a) < len(b):
        bl = lb-la
        for k in range(bl):
            a = '0'+a
    elif len(b) < len(a):
        bl = la-lb
        for l in range(bl):
            b = '0'+b

    

    while i >= -1:
        if a[i] == '1':
            if b[i] == '1':
                if carry == 1:
                    answer = 1
                    carry = 1
                    result = str(answer) + result
                else:
                    answer = 0
                    carry = 1
                    result = str(answer) + result
                
                

            elif b[i] == '0':
                if carry == 1:
                    answer = 0
                    carry = 1
                    result = str(answer) + result
                else:
                    answer = 1
                    carry = 0
                    result = str(answer) + result
               
            i -=1
        elif a[i] == '0':
            if b[i] == '1':
                if carry == 1:
                    answer = 0
                    carry = 1
                    result = str(answer) + result
                else:
                    answer = 1
                    carry = 0
                    result = str(answer) + result
                
            elif b[i] == '0':
                if carry == 1:
                    answer = 1
                    carry = 0
                    result = str(answer) + result
                else:
                    answer = 0
                    carry = 0
                    result = str(answer) + result
                
            i -=1
        
    return result




a = '1011'
b = '1010'
# 
print(addbinary(a,b))   