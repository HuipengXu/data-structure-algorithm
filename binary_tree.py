# @Time    : 2019/2/2 22:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import Optional


class Node:
    """
    二叉树节点类
    """

    def __init__(self, val: Optional[float] = None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Binary Tree Node: %.2f>" % self.val


class BinaryTree:
    """
    链式二叉查找树，不存在重复节点
    """

    def __init__(self, root: Optional[float] = None):
        self.root = Node(root)

    def insert(self, val: float):
        if self.root is None:
            self.root = Node(val)
        node = self.root
        while True:
            if node.val < val:
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

    def pre_order(self):
        node = self.root
        nodes_list = []
        rights = []
        while node:
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


if __name__ == "__main__":
    bt = BinaryTree()
    # for i in [1, 6, 0, 2, 5, 7]:
    #     bt.insert(i)
    print(bt.pre_order())
