def average(salary):
    sum = 0
    minVal = salary[0]
    maxVal = salary[0]

    # Finding min and max from this salry array
    for i in range(len(salary)):
        if salary[i] < minVal:
            minVal = salary[i]
        if salary[i] > maxVal:
            maxVal = salary[i]
    
    # Removing min and max from the array
    salary.remove(minVal)
    salary.remove(maxVal)

    # Finding sum of all other numbers
    for i in salary:
        sum +=i
    
    #  Finding avg of the number 
    avg = sum/(len(salary))
    # Returning the avg value
    return avg



salary = [4000,3000,1000,2000]

#Calling the function
print(average(salary))

