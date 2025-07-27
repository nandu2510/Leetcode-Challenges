"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        if root is None:
            return []
        def pre(node):
            res.append(node.val)
            for child in node.children:
                pre(child)
        pre(root)
        return res