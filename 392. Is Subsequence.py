class Solution:
    def isSubsequence(self, s, t):
        w=[]
        x=0
        for i in range(len(s)):
            a=False
            
            for j in range (x,len(t)):
                if s[i]==t[j]:
                    a=True
                    x+=1
                    break
                else:
                    x+=1
            w.append(a)
        if False in w:
            a=False
        else:
            a=True
        return a
        
        
l=Solution()
s="abc"
t="ayugfc"
print(l.isSubsequence(s,t))