class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        a=(nums1 + nums2)
        print(a)
        a.sort()
        print(a)
        if len(a)%2!=0:
            b=len(a)//2
            print(b)
            median=a[b]
        else:
            print(len(a))
            b=int(((len(a))/2)-1)
            print(b)
            c=int(a[b])
            d=int(a[b+1])
            median=(c+d)/2
        return median
        
        

l=Solution()
nums1=[1,3]
nums2=[2,4]
print(l.findMedianSortedArrays(nums1,nums2))