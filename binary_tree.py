# @Time    : 2019/2/2 22:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import Optional


class Node:
    """
    二叉树节点类
    """

    def __init__(self, val: Optional[int] = None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Binary Tree Node: %d>" % self.val


class BinarySearchTree:
    """
    链式二叉查找树，支持重复数据
    """

    def __init__(self, root: Optional[int] = None):
        self.root = Node(root)

    def insert(self, val: int):
        if self.root.val is None:
            self.root = Node(val)
        else:
            node = self.root
            while True:
                if node.val <= val:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(val)
                        break
                else:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(val)
                        break

    def _find(self, val: int):
        nodes = []
        node = self.root
        parent = loc = None
        while node:
            if val < node.val:
                parent = node
                loc = 'left'
                node = node.left
            elif val > node.val:
                parent = node
                loc = 'right'
                node = node.right
            else:
                nodes.append((parent, loc, node))
                parent = node
                loc = 'right'
                node = node.right
        return nodes

    def delete(self, val: int):
        """
        完全通过更新引用实现
        """
        nodes = self._find(val)
        if len(nodes) == 0: raise ValueError('%d is not in binary search tree' % val)

        def update(loc: str, parent: Node, child: Node = None):
            if loc == 'left':
                parent.left = child
            else:
                parent.right = child

        for parent, loc, node in nodes[::-1]:
            if not (node.left or node.right):
                update(loc, parent)
            elif node.left and not node.right:
                update(loc, parent, node.left)
            elif node.right and not node.left:
                update(loc, parent, node.right)
            else:
                min_child = node.right
                min_child_parent = node
                while min_child.left:
                    min_child_parent = min_child
                    min_child = min_child.left
                update(loc, parent, min_child)
                min_child.left = node.left
                min_child.right = node.right if node.right is not min_child else None
                min_child_parent.left = None

    def delete_(self, val: int):
        """
        通过替换数据实现
        """
        nodes = self._find(val)
        if len(nodes) == 0: raise ValueError('%d is not in binary search tree' % val)

        for parent, _, node in nodes[::-1 ]:
            # 待删除节点有两个子节点
            if node.left and node.right:
                min_child = node.right
                min_child_parent = node
                while min_child.left:
                    min_child_parent = min_child
                    min_child = min_child.left
                node.val = min_child.val
                node = min_child
                parent = min_child_parent

            # 待删除的节点没有子节点或只有一个
            if node.left:
                node_child = node.left
            elif node.right:
                node_child = node.right
            else:
                node_child = None

            if parent is None:
                self.root = node_child
            elif parent.left is node:
                parent.left = node_child
            else:
                parent.right = node_child

    def find(self, val: int):
        nodes = self._find(val)
        return nodes

    def pre_order(self):
        node = self.root
        nodes_list = []
        rights = []
        while True:
            nodes_list.append(node.val)
            if node.left:
                if node.right:
                    rights.append(node.right)
                node = node.left
            elif node.right:
                node = node.right
            else:
                if len(rights) == 0:
                    break
                node = rights.pop()
        return nodes_list

    def pre_order_recursive(self):
        nodes_list = []

        def recurse(root: Node):
            if root is not None:
                nodes_list.append(root.val)
                recurse(root.left)
                recurse(root.right)

        recurse(self.root)
        return nodes_list

    def in_order(self):
        nodes_list = []

        def recurse(root: Node):
            if root is not None:
                recurse(root.left)
                nodes_list.append(root.val)
                recurse(root.right)

        recurse(self.root)
        return nodes_list

    def post_order(self):
        nodes_list = []

        def recurse(root: Node):
            if root is not None:
                recurse(root.left)
                recurse(root.right)
                nodes_list.append(root.val)

        recurse(self.root)
        return nodes_list


if __name__ == "__main__":
    bst = BinarySearchTree()
    arr1 = [33, 16, 50, 13, 18, 34, 58, 34, 15, 17, 25, 51, 66, 19, 27, 55]
    arr2 = [10, 9, 8, 7, 6, 5]
    for i in arr2:
        bst.insert(i)
    print(bst.pre_order_recursive())
