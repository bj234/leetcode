"""
Try all n possible rotations and find minimum cost of individual elements. 
Thier sum and cost for rotation is used to find minimum cost for each rotation. 
Then minimum value is found by comparing total costs of all such rotations (even 0).
ret=min(ret,s+i*x)

Complexity
Time complexity: O(n^2) 
Space complexity: O(n)
"""
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n=len(nums)
        minarr=[]
        ret=10**20
        for i in range(n):minarr.append(nums[i])
        for i in range(n):
            s=0
            for j in range(n):
                minarr[j]=min(minarr[j],nums[(i+j)%n])
                s+=minarr[j]
            ret=min(ret,s+i*x)
        return ret  
