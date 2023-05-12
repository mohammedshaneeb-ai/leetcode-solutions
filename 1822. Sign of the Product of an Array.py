class Solution:
    def arraySign(self, nums):
        prod = nums[0]

        for i in range(1,len(nums)):
            prod *=nums[i]
        
        return self.signFunc(prod)    
    def signFunc(self,num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
