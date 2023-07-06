class Solution {
public:
    bool isvalid(int mid,int target,vector<int>& nums){
        int s=0,n=nums.size();
        for(int i=0;i<mid;i++) s+=nums[i];
        if(s>=target) return true;
        int i=0;
        while(i+mid<n){
            s-=nums[i];
            s+=nums[i+mid];
            i++;
            if(s>=target) return true;
        }
        return false;
    }
    int minSubArrayLen(int target, vector<int>& nums) {
        int l=0,r=nums.size(),ret=0;
        while(l<=r){
            int mid=(l+r)/2;
            if(isvalid(mid,target,nums)){
                ret=mid;
                r=mid-1;
            }
            else l=mid+1;
        }
        return ret;
    }
};
