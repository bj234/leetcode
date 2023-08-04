class Solution:
    def minDeletions(self, s: str) -> int:
        c=Counter(s)
        arr=[]
        for k in c:
            arr.append(c[k])
        arr.sort(reverse=True)
        count=0
        for i in range(1,len(arr)):
            if arr[i]>=arr[i-1] and arr[i-1]!=0:
                temp=arr[i]-arr[i-1]+1
                count+=temp
                arr[i]-=temp
            elif arr[i-1]==0:
                count+=arr[i]
                arr[i]=0
        return count
