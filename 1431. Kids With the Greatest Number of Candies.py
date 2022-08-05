class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        a=max(candies)
        print(a)
        w=[]
        for i in range(len(candies)):
            s=int(candies[i])+extraCandies
            if s>=a:
                w.append(True)
            else:
                w.append(False)
        return w

if __name__=="__main__":
    l=Solution()
    candies=[1,7,1,8,4,2,1,1]
    extraCandies=1
    print(l.kidsWithCandies(candies,extraCandies))               