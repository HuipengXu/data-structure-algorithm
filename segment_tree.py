# @Time    : 2019/4/17 16:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Union, Optional


class SegmentTreeNode:

    def __init__(self, val: Union[int, float], start: int, end: int,
                 left: Optional['SegmentTreeNode'] = None,
                 right: Optional['SegmentTreeNode'] = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def __repr__(self):
        return '<SegmentTreeNode: {}>'.format(self.val)


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.root = self._build_tree(nums, 0, len(nums) - 1)

    def _build_tree(self, nums: List[int], start: int, end: int) -> Optional[SegmentTreeNode]:
        node = SegmentTreeNode(min(nums[start: end + 1]), start, end)
        if start == end: return node
        mid = start + ((end - start) >> 1)
        node.left = self._build_tree(nums, start, mid)
        node.right = self._build_tree(nums, mid + 1, end)
        return node

    def range_min(self, start: int, end: int,
                  node: Optional[SegmentTreeNode]=None) -> Optional[Union[int, float]]:
        if end < start: return
        node = node or self.root
        if start == node.start and end == node.end:
            return node.val
        if start <= node.left.end and end >= node.right.start:
            return min(self.range_min(start, node.left.end, node.left),
                       self.range_min(node.right.start, end, node.right))
        elif start > node.left.end:
            return self.range_min(start, end, node.right)
        else:
            return self.range_min(start, end, node.left)

    def update(self, index: int, val: Union[int, float],
               node: Optional[SegmentTreeNode]=None) -> Optional[int]:
        node = node or self.root
        if not node.start <= index <= node.end: return None
        if index == node.start == node.end:
            node.val = val
            return val
        if index <= node.left.end:
            new_val = self.update(index, val, node.left)
            node.val = min(new_val, node.right.val)
            return node.val
        else:
            new_val = self.update(index, val, node.right)
            node.val = min(new_val, node.left.val)
            return node.val


if __name__ == '__main__':
    nums = [1, 2, 6, 10, 8, 3]
    st = SegmentTree(nums)
    print(st.range_min(0, 5))
    st.update(0, 9)
    print(st.range_min(0, 5))