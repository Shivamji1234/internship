class Solution:
    def canJump(self, nums) :
        jump = nums[0]
        for i in range(1,len(nums)):
            if jump == 0:
                return print("false")
            jump=nums[i]
            
        return print("True")
nums=[1,2,3,4,1,5]
l=Solution()
l.canJump(nums)