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
        

obj = Solution()


nums = [-1,-2,-3,-4,3,2,1]
print(obj.arraySign(nums))

nums = [1,5,0,2,-3] 
print(obj.arraySign(nums))

nums = [-1,1,-1,1,-1]
print(obj.arraySign(nums))

