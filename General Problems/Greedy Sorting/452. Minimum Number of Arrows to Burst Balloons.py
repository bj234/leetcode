class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda k:k[1])
        #sort based on end cordinate, as it is most optimal to choose the rightmost option possible.
        #This can help in maximizing the available points
        n=len(points)
        i=0
        #initialy we have to collect the shortest end(right) point
        count=1
        temp=points[0][1]
        while i<n:
            #Greedily collect as many points as possible if the arrow is shot at points[i][0]
            while i<n and points[i][0]<=temp:i+=1
            if i<n:
                count+=1
                temp=points[i][1]
        return count
