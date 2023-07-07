class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int i=0,j=0,maxconf=1,n=answerKey.size();
        int t=0,f=0;
        if(char(answerKey[0])=='T') t=1;
        else f=1;
        //window size=j-i+1
        //confusion=max(t,f)+k
        while(i<n and j<n){
            while(j<n-1 and max(t,f)+k>=j-i+1){
                j++;
                if(answerKey[j]=='T') t++;
                else f++;
                maxconf=max(maxconf,max(t,f)+k);
            }
            while(i<n and max(t,f)+k<j-i+1){
                if(answerKey[i]=='T') t--;
                else f--;
                i++;
                maxconf=max(maxconf,max(t,f)+k);
            }
            if(j==n-1) break;
        }
        maxconf=max(maxconf,max(t,f)+k);
        int s=answerKey.size();
        return min(maxconf,s);     
    }
};
