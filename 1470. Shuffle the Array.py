from pandas import array


class Solution:
    def shuffle(self, nums, n: int):
        a1=nums[:n]
        a2=nums[n:]
        a=[]
        for i in range (n):
            a.append(a1[i])
            a.append(a2[i])
        return a


if __name__=="__main__":
    l=Solution()
    nums=[]
    n=int(input())
    nums=[2,5,1,3,4,7]
    
    print(l.shuffle(nums,n))