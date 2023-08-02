class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n=len(coins)
        dp=dict()
        def dfs(a,i):
            if a==amount:return 1
            if a>amount or i==n:return 0
            if (a,i) in dp:return dp[(a,i)]
            #select the coin on index i.
            #Note: this wont create an infinite loop as the amount is capped
            x=dfs(a+coins[i],i)
            #going for the next recursion       
            y=dfs(a,i+1)
            dp[(a,i)]=x+y
            return x+y
        return dfs(0,0)
