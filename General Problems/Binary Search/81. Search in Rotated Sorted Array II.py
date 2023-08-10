class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        # Find the index with the smallest value
        # If all values are same this function returns 0 (leftmost index)
        def smallindex(nums):
            l=0
            r=n-1
            smallest=10**9
            ret=0
            while l<=r:               
                mid=(l+r)//2
                # If the element to the left of mid > mid, then mid is the smallest value
                if nums[(mid-1)%n]>nums[mid]:return mid
                if nums[mid]<nums[r]:
                  #The smallest value is not to right of mid, if smallest value is to the right of mid then nums[r] will be <= nums[mid]
                    if nums[mid]<=smallest:
                        smallest=nums[mid]
                        ret=mid
                    r=mid-1
                elif nums[mid]>nums[r]:
                    if nums[r]<=smallest:
                        smallest=nums[r]
                        ret=r
                    l=mid+1
                else:
                    if nums[(r-1)%n]>nums[r]:return r
                    else:r-=1
            return ret
        l=smallindex(nums)
        r=l+n-1
        print(l)
        while l<=r:
            mid=((l+r)//2)
            if nums[mid%n]==target:return True
            elif nums[mid%n]>target:
                r=mid-1
            else:l=mid+1
        return False
