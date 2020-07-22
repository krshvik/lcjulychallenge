# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    di = {}
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.di = {}
        if root is None:
            return []
        self.traverse(root,0)
        arr = []
        maxd = max(self.di)
        i = 0 
        while i <= maxd:
            if i%2 == 0:
                arr.append(self.di[i])
            else:
                arr.append(self.di[i][::-1])
            i = i + 1
        return arr 
    
    def traverse(self,cnode,lvl):
        if cnode is None:
            return
        if cnode.left is not None:
            self.traverse(cnode.left,lvl+1)
        if lvl not in self.di:
            self.di[lvl] = []
        self.di[lvl].append(cnode.val)
        if cnode.right is not None:
            self.traverse(cnode.right,lvl+1)
        return 