class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def ispos(answerKey,k,mid):
            temp=[]
            for i in range(mid):temp.append(answerKey[i])
            #print(mid,temp)
            t,f=0,0
            for i in range(len(temp)):
                if temp[i]=="T":t+=1
                else:f+=1
            if max(t,f)+k>=mid:return True
            i=0
            while i+mid<len(answerKey):
                if temp[0]=="T":t-=1
                else:f-=1
                del temp[0]
                temp.append(answerKey[i+mid])
                if temp[-1]=="T":t+=1
                else:f+=1
                #print(temp)
                if max(t,f)+k>=mid:return True
                i+=1
            return False
        l=1
        r=len(answerKey)
        index=-1
        while l<=r:
            mid=(l+r)//2
            if ispos(answerKey,k,mid):
                index=mid
                l=mid+1
            else:r=mid-1
        return index
