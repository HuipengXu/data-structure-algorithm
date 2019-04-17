# @Time    : 2019/4/17 9:19
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import Optional


class BinaryIndexedTree:

    def __init__(self, length: int, nums: Optional[list] = None):
        self.data = [0] * (length + 1)
        if nums is not None: self._init_data(nums, length)

    def _init_data(self, nums: list, length: int) -> None:
        self.data[1:] = nums
        for i in range(1, length + 1):
            j = i + self._lowbit(i)
            if j < length + 1: self.data[j] += self.data[i]

    def _lowbit(self, i: int) -> int:
        return (-i) & i

    def update(self, i: int, val: int) -> bool:
        if i >= len(self.data): return False
        while i < len(self.data):
            self.data[i] += val
            i += self._lowbit(i)
        return True

    def sum(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self.data[i]
            i -= self._lowbit(i)
        return ans

    def range_sum(self, i: int, j: int) -> int:
        return self.sum(j) - self.sum(i - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    bit = BinaryIndexedTree(len(nums))
    for i in nums:
        bit.update(i, i)
    # print(bit.data)
    # bit1 = BinaryIndexedTree(len(nums), nums)
    # print(bit1.data)
    print(bit.range_sum(2, 4))
