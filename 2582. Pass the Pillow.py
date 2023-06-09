class Solution:
    def passThePillow(self,n,time):          
        cycles = time //2 (2*(n-1))
        direction = 1 if cycles % 2 == 0 else -1
		index = 1 if direction == 1 else n
	
		remaining_seconds = time % (2 * (n - 1))
        if remaining_seconds <= n - 1:
			index += direction * remaining_seconds
		else:
			index += direction * (n - 1) - direction * (remaining_seconds - (n - 1))
		
		if direction == -1:
			index = n - index + 1
		return index
    

obj = Solution()

# Example 1
n = 4
time = 5
#Expected Output: 2

# Example 1
n = 3
time = 2
#EXpected Output: 3


print(obj.passThePillow(n,time))