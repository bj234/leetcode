class Solution {
public:
    bool ispossible(vector<int>& nums,int mid){
        // binary search
        int l=0,r=mid,count1=0;
        for(int i=0;i<=r;i++){
            if(nums[i]==1) count1++;
        }
        if(count1>=mid) return true;
        while(r<nums.size()-1){
            if(nums[l]==1) count1-=1;
            l++;
            r++;
            if(nums[r]==1) count1+=1;
            if(count1>=mid) return true;
        }
        return false;
    }
    int longestSubarray(vector<int>& nums) {
        int l=0,r=nums.size()-1,ret=-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(ispossible(nums,mid)){
                ret=mid;
                l=mid+1;
            }
            else r=mid-1;
        }
        return ret;
    }
};
