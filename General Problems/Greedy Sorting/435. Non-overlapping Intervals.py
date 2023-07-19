class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:k[1])
        #sort coordinates based on increasing end points
        n=len(intervals)
        i=0
        j=1
        count=0
        while i<n-1 and j<n:
            #i, j are left, right pointers. when i1>j0 intersection occurs. So point j is discarded and j and count is incremented
            # else check shifts to next point
            # Same effect can also be obtained in while loop instead of if statement.
            if intervals[i][1]>intervals[j][0]:
                count+=1
                j+=1
            else:
                j+=1
                i=j-1
        return count
