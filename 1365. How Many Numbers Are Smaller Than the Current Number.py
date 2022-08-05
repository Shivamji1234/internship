class Solution:
    def smallerNumbersThanCurrent(self, nums):
        w=[]
        for i in range(len(nums)):
            a=int(nums[i])
            s=0
            for j in range(len(nums)):
                if a>int(nums[j]):
                    s+=1
                else:
                    pass
                    
            
            w.append(s)
        return w

l=Solution()
nums=[8,1,2,2,3]
print(l.smallerNumbersThanCurrent(nums))