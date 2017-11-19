class Solution(object):
    def isSameTree(self, p, q):
        if p and not q:
            return False
        if q and not p:
            return False
        
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)