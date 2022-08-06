class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
            def findMaxSum(i, j):       
                maxVal= 0
                summ = 0
                for newJ in range(i, min(i+k, j+1)):
                    maxVal = max(maxVal, arr[newJ])
                    summ = max(summ, maxVal*(newJ - i + 1) + findMaxSum(newJ+1, j))
                return summ
                
            return findMaxSum(0, len(arr)-1)

l=Solution()
arr=[1,15,7,9,2,5,10]
k=3
print(l.maxSumAfterPartitioning(arr,k))