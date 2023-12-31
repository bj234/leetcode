class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        //two pointer
        int i=0,j=0,n=nums.size(),count1=0;
        if(count(nums.begin(),nums.end(),1)==n) return n-1;
        if(nums[0]==1) count1=1;
        int maxcount=count1;
        //zerocount=j-i+1-count1
        while(i<n and j<n){
            while(j<n-1 and j-i+1-count1<2){
                j++;
                if(nums[j]==1) count1++;
                maxcount=max(count1,maxcount);
            }
            while(i<n and j-i+1-count1>=2){
                if(nums[i]==1) count1--;
                i++;
            }
            j++;
            if(j<n and nums[j]==1) count1++;
            maxcount=max(count1,maxcount);
        }
        return maxcount;
    }
};
