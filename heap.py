# @Time    : 2019/2/13 17:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Optional, Tuple


class BigTopHeap:

    def __init__(self, arr: list):
        self.length = len(arr) + 1
        self.heap = [None] * self.length
        self._heapify(arr)

    def _one_step_heapify(self, idx: int, end: int):
        while True:
            if 2 * idx >= end:
                break
            elif 2 * idx + 1 >= end or self.heap[2 * idx] > self.heap[2 * idx + 1]:
                max_idx = 2 * idx
            else:
                max_idx = 2 * idx + 1
            if self.heap[idx] > self.heap[max_idx]:
                break
            self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
            idx = max_idx

    def _heapify(self, arr: list):
        """
        从上到下堆化
        """
        self.heap[1:] = arr[:]
        non_leaf = (self.length - 1) // 2
        for idx in range(non_leaf, 0, -1):
            self._one_step_heapify(idx, self.length)

    def insert(self, val: int):
        """
        从下到上堆化
        """
        self.heap.append(val)
        idx = len(self.heap) - 1
        while True:
            parent_idx = idx // 2
            if parent_idx == 0 or self.heap[parent_idx] > self.heap[idx]:
                break
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        self.length += 1

    def _delete_top(self, end: int):
        self.heap[1], self.heap[end] = self.heap[end], self.heap[1]
        self._one_step_heapify(1, end)

    def delete_top(self):
        if self.length == 1:
            return None
        self._delete_top(self.length - 1)
        self.length -= 1
        return self.heap.pop()

    def sort(self):
        for i in range(1, self.length - 1):
            self._delete_top(self.length - i)
        return self.heap[1:]


class SmallTopHeap:
    """
    为 dijkstra 服务
    """

    def __init__(self):
        self.heap: List[Optional[list]] = [None]
        self.length = 1

    def _up_heapify(self, idx: int, val: list):
        """
        从下往上堆化
        """
        while True:
            parent_idx = idx // 2
            if parent_idx == 0 or self.heap[parent_idx][1] <= val[1]:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx

    def insert(self, val: list):
        self.heap.append(val)
        self._up_heapify(self.length, val)
        self.length += 1

    def poll(self) -> Optional[list]:
        if self.length == 1: return None
        self.heap[1], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[1]
        vertex = self.heap.pop()
        self.length -= 1
        idx = 1
        # 从上往下堆化
        while True:
            left, right = 2 * idx, 2 * idx + 1
            if left >= self.length:
                break
            elif right >= self.length or self.heap[left][1] <= self.heap[right][1]:
                swap_idx = left
            else:
                swap_idx = right
            if self.heap[idx][1] < self.heap[swap_idx][1]:
                break
            self.heap[idx], self.heap[swap_idx] = self.heap[swap_idx], self.heap[idx]
            idx = swap_idx
        return vertex

    def update(self, val: list) -> bool:
        for i in range(1, self.length):
            if self.heap[i][0] == val[0]:
                self.heap[i][1] = val[1]
                self._up_heapify(i, val)
                return True
        return False

    def is_empty(self) -> bool:
        if self.length == 1: return True
        return False


if __name__ == "__main__":
    a = [7, 5, 19, 8, 4, 1, 20, 13, 16]
    bth = BigTopHeap(a)
    # print(bth.sort())
    for i in range(10):
        print(bth.delete_top())
    print(bth.heap)
