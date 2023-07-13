class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Time:O(n)
        #Space:O(n)
        d=Counter(citations)
        m=max(citations)
        count=[0]*(m+1)
        s=0
        for i in range(m,-1,-1):
            s+=d[i]
            count[i]=s
        #print(count)
        #No need of binary search as already O(n) is used for creating dict and prefix array
        flag=0
        for i in range(m+1):
            if count[i]>=i:flag=i
        return flag
