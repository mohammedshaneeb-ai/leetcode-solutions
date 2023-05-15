def average(salary):
    sum =0
    minVal = salary[0]
    maxVal = salary[0]
    for i in range(len(salary)):
        if salary[i] < minVal:
            minVal = salary[i]
        if salary[i] > maxVal:
            maxVal = salary[i]
    
    salary.remove(minVal)
    salary.remove(maxVal)

    for i in salary:
        sum +=i
    avg = sum/(len(salary))
    return avg



# print(salary)
salary = [4000,3000,1000,2000]

print(average(salary))
# print(salary)

