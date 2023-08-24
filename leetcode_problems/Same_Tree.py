from dtos import Node
class Solution:
    def isSameTree(self, p: Optional[Node], q: Optional[Node]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if p.val != q.val:
            return False