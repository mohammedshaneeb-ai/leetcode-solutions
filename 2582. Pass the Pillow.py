class Solution:
    def passThePillow(self,n,time):
        cycles = time //2 (2*(n-1))
        direction = 1 if cycles % 2 == 0 else -1
		index = 1 if direction == 1 else n
		remaining_seconds = time % (2 * (n - 1))
