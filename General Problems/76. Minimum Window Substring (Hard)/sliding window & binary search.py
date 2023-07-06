class Solution:
    #Time: O(n logn)
    #Space: O(1) 
    #We only use a dictionary of size max 52
    def minWindow(self, s: str, t: str) -> str:
        tdict=Counter(t)
        print(tdict)
        def validatedict(d):
            for k in tdict:
                if d[k]<tdict[k]:return False
            return True
        def checkvalid(mid):
            d=Counter(s[:mid])
            if validatedict(d):return s[:mid]
            for i in range(len(s)-mid):
                d[s[i]]-=1
                d[s[i+mid]]+=1
                if validatedict(d):return s[i+1:i+1+mid]
            return ""
        l=1
        r=len(s)
        ret=""
        while l<=r:
            mid=(l+r)//2
            temp=checkvalid(mid)
            if len(temp)>0:
                r=mid-1
                ret=temp
            else:l=mid+1
        return ret
            
