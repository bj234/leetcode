class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minlen=INT_MAX,i=0,j=0,s=nums[0],n=nums.size();
        if(s>=target) return 1;
        while(i<n and j<n){
            while(j<n-1 and s<target){
                j++;
                s+=nums[j];
                if(s>=target) minlen=min(minlen,j-i+1);
            }
            while(i<n and s>=target){
                s-=nums[i];
                i++;
                if(s>=target) minlen=min(minlen,j-i+1);
            }
            if(j==n-1) break;
        }
        if(minlen==INT_MAX) return 0;
        return minlen;
    }
};
