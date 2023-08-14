# Solution 1, Recursion, caching by dictionary
# Time: O(n)
# Space: O(n)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=dict()
        def dfs(i):
            if i>=n:return True
            if i==n-1:return False
            if i in dp:return dp[i]
            a,b,c=False,False,False
            if nums[i]==nums[i+1]:a=dfs(i+2)
            if i<n-2:
                if nums[i]==nums[i+1] and nums[i]==nums[i+2]:
                    b=dfs(i+3)
                if nums[i]+1==nums[i+1] and nums[i]+2==nums[i+2]:
                    c=dfs(i+3)
            dp[i]=a or b or c
            return dp[i]
        ret=dfs(0)
        #print(dp)
        return ret


# Solution 2, Iterative bottom-up
# Time:O(n)
# Space:O(1)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        #Initialising a,b,c to True to simulate out of bound to right as True
        a,b,c=True,True,True
        # We use four dummy variables as aliased for the dp with index
        #dp[i]=ret
        #dp[i+1]=a
        #dp[i+2]=b
        #dp[i+3]=c
        for i in range(n-1,-1,-1):
            #newa,b,c values initialised to False in each iteration, incase if conditions are not met they have to be False
            newa,newb,newc=False,False,False
            if i<n-1:
                if nums[i]==nums[i+1]:
                    newa=b
            if i<n-2:
                if nums[i]==nums[i+1] and nums[i]==nums[i+2]:
                    newb=c
                if nums[i]+1==nums[i+1] and nums[i]+2==nums[i+2]:
                    newc=c
            if newa or newb or newc:ret=True
            else:ret=False
            # Value transfer for next iteration
            c=b
            b=a
            a=ret
        return a
