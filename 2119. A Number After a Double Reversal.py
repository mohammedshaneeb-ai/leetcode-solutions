def isSameAfterReversals(num):
    reversed1 = 0
    reversed2 = 0
    flag = 0
    nums = num
    while num != 0:
        digit = num % 10
        if flag == 0:
            if digit == 0:
                num //= 10
                continue
            else:
                flag =1
        
        reversed1 = reversed1 * 10 + digit
        num //= 10

    while reversed1 != 0:
        digit = reversed1 % 10
        reversed2 = reversed2 * 10 + digit
        reversed1 //= 10

    print(nums,reversed2)
    if reversed2 == nums:
        return True
    else:
        return False

    
    

print(isSameAfterReversals(00))