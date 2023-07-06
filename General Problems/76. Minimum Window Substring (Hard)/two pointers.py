class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict=Counter(t)
        d=Counter(s[0])
        i=0
        j=0
        ret=""
        n=len(s)
        minlen=10**9
        def validate(d):
            for k in tdict:
                if d[k]<tdict[k]:return False
            return True
        while i<n and j<n:
            while j<n-1 and not validate(d):
                j+=1
                d[s[j]]+=1
            if validate(d) and j-i+1<minlen:
                minlen=min(minlen,j-i+1)
                ret=s[i:j+1]
            while i<n and validate(d):
                d[s[i]]-=1
                i+=1
                if validate(d) and j-i+1<minlen:
                    minlen=min(minlen,j-i+1)
                    ret=s[i:j+1]
            if j==n-1:
                if validate(d) and j-i+1<minlen:
                    minlen=min(minlen,j-i+1)
                    ret=s[i:j+1]
                break
        return ret
        


            
