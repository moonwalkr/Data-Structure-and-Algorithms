class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.is_valid(root, -math.inf, math.inf)

    def is_valid(self, root, min_val, max_val):
        if root is None:
            return True
        else:
            return (root.val > min_val and root.val < max_val and
                    self.is_valid(root.left, min_val, root.val)
                    self.is_valid(root.right, root.val, max_val))