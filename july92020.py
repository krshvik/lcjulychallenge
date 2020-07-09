# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    di = {}
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.di = {}
        mwidth = 0 
        self.travel(root,'1',0)
        for d in self.di:
            a = self.di[d]
            val = a[len(a)-1]-a[0] + 1
            if val > mwidth:
                mwidth = val 
        return mwidth 
    
    def travel(self,cnode,bits,lvl):
        
        if cnode is None:
            return
        
        b = int(bits,2)
        if lvl not in self.di:
            self.di[lvl] = []
        self.di[lvl].append(b)
        
        if cnode.left is not None:
            self.travel(cnode.left,bits+'0',lvl+1)
        
        if cnode.right is not None:
            self.travel(cnode.right,bits+'1',lvl+1)
        
        return 