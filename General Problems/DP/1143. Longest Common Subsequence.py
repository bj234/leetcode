class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=dict()
        def dfs(i,j):
            if i==m or j==n:return 0
            if (i,j) in dp:return dp[(i,j)]
            if text1[i]==text2[j]:
                dp[(i,j)]=1+dfs(i+1,j+1)
                return dp[(i,j)]
            a=dfs(i+1,j)
            b=dfs(i,j+1)
            dp[(i,j)]=max(a,b)
            return dp[(i,j)]
        return dfs(0,0)
