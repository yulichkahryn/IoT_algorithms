class Tree:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.height = 0

        def get_dif(self):
            lft_sub = 0
            if self.left is not None:
                lft_sub = self.left.height
            rght_sub = 0
            if self.right is not None:
                rght_sub = self.right.height
            return lft_sub - rght_sub

        def is_balanced(self):
            return (abs(self.get_dif()) < 2)

        def recalc(self):
            lft_sub = 0
            if self.left is not None:
                lft_sub = self.left.height
            rght_sub = 0
            if self.right is not None:
                rght_sub = self.right.height
            self.height = max(lft_sub, rght_sub) + 1

    def __init__(self):
        self.root = None

    def rotate_right(self, node) -> Node:
        if node is None:
            return None
        left_child = node.left
        LR = left_child.right
        node.left = LR
        left_child.right = node
        node.recalc()
        left_child.recalc()
        return left_child

    def rotate_left(self, node) -> Node:
        if node is None:
            return None
        right_child = node.right
        RL = right_child.left
        node.right = RL
        right_child.left = node
        node.recalc()
        right_child.recalc()
        return right_child

    def insert_val(self, node, val) -> Node:
        if node is None:
            return self.Node(val)
        if node.val > val:
            node.left = self.insert_val(node.left, val)
        elif node.val < val:
            node.right = self.insert_val(node.right, val)

        if not node.is_balanced():
            if node.val > val:  # L
                if node.left.val < val:  # LR
                    node.left = self.rotate_left(node.left)
                # LL
                node = self.rotate_right(node)
            else:  # R
                if node.right.val > val:  # RL
                    node.right = self.rotate_right(node.right)
                # RR
                node = self.rotate_left(node)

        return node

    def insert(self, val):
        self.root = self.insert_val(self.root, val)

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        print(node.val, end=' ')
        self.dfs(node.right)
        if not node.is_balanced():
            print("That's great(joke)")

    def print(self):
        self.dfs(self.root)
        print()


tree = Tree()

tree.insert(2142)
tree.insert(241)
tree.insert(213)
tree.insert(245)
tree.insert(9)
tree.insert(0)
tree.insert(10)

tree.print()
