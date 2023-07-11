# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time Complexity: O(n^2) i guess maybe O(nh) h=height of the tree
#Space:O(h) to O(n) when tree becomes linked list
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:return []
        if k==0:return [target.val]
        arr=[]
        def dfs(node,path):
            if node:
                if node.val==target.val:
                    arr.append(path.copy())
                    return 
                if node.left:
                    path.append(node.left)
                    dfs(node.left,path)
                    path.pop()
                if node.right:
                    path.append(node.right)
                    dfs(node.right,path)
                    path.pop()
        dfs(root,[root])
        pathval=[]
        for node in arr[0]:pathval.append(node.val)
        #print(pathval)
        #Values of path from root to target is stored in this set inorder to avoid traversing via BFS through this
        #If we traverse through these values we will incorrectly judge the node distance
        pathvalset=set(pathval)
        t=target.val
        ret=set()
        def bfs(node,targetlevel):
            q=[[node,targetlevel]]
            while q:
                temp=q.pop(0)
                tempnode=temp[0]
                level=temp[1]
                #print(tempnode.val,level)
                if level==0:ret.add(tempnode.val)
                if level<0:break
                if tempnode.val!=target.val:
                    if tempnode.left and tempnode.left.val!=t and tempnode.left.val not in pathvalset:
                        q.append([tempnode.left,level-1])
                    if tempnode.right and tempnode.right.val!=t and tempnode.right.val not in pathvalset:
                        q.append([tempnode.right,level-1])
        if target.left:bfs(target.left,k-1)
        if target.right:bfs(target.right,k-1)
        #traversing along the path we got from root to target via DFS
        for i in range(1,min(k+1,len(arr[0]))):
            #print("i= ",i)
            node=arr[0][len(arr[0])-1-i]
            targetlevel=k-i
            #print(node.val,targetlevel)
            bfs(node,targetlevel)
        return list(ret)
