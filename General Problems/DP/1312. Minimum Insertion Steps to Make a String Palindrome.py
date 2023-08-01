class Solution:
    def minInsertions(self, s: str) -> int:
        dp=dict()
        def dfs(i,j):
            if i>j:return 0
            if (i,j) in dp:return dp[(i,j)]
            if s[i]==s[j]:
                dp[(i,j)]=dfs(i+1,j-1)
                return dp[(i,j)]
            a=dfs(i+1,j)
            b=dfs(i,j-1)
            ret=1+min(a,b)
            dp[(i,j)]=ret
            return ret
        return dfs(0,len(s)-1)
