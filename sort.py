from typing import List
import random

# 冒泡排序
def bubble_sort(nums: list):
    if nums:
        length = len(nums)
        if length != 1:
            for i in range(length):
                swap_times = 0
                for j in range(length - i - 1):
                    if nums[j] > nums[j+1]:
                        swap_times += 1
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                if swap_times == 0:
                    break
# 插入排序
def insert_sort(nums: list):
    if not nums:
        return None
    length = len(nums)
    if length == 1:
        return None
    for i in range(1, length): 
        for j in range(i):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[j+1: i+1] = nums[j: i] 
                nums[j] = temp

# 选择排序
def select_sort(nums: list):
    if not nums:
        return None
    length = len(nums)
    if length == 1:
        return None
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != j:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
# 归并排序
def merge_sort0(nums: list):
    length = len(nums)
    def merge_sort_c(nums: list, end: int):
        if end == 1:
            return nums
        median = end // 2
        first_half = merge_sort_c(nums[:median], len(nums[:median]))
        second_half = merge_sort_c(nums[median:], len(nums[median:]))
        return merge(first_half, second_half)
    def merge(first: list, second: list):
        merge_nums = []
        while first and second:
            if first[0] <= second[0]:
                merge_nums.append(first.pop(0))
            else:
                merge_nums.append(second.pop(0))
        if first:
            merge_nums.extend(first)
        else:
            merge_nums.extend(second)
        return merge_nums
    return merge_sort_c(nums, length)

# 归并排序, 利用下标
def merge_sort1(nums: list):
    def merge_sort_c(nums: list, p: int, r: int):
        if (r - p) > 1 :
            q = p + ((r - p) >> 1)
            merge_sort_c(nums, p, q)
            merge_sort_c(nums, q, r)
            merge(nums, p, q, r)
    def merge(nums: list, p: int, q: int, r: int):
        j, k = p, q
        tmp = [0] * (r - p)
        i = 0
        while (j < q) and (k < r):
            if nums[j] <= nums[k]:
                tmp[i] = nums[j]
                j += 1
            else:
                tmp[i] = nums[k]
                k += 1
            i += 1
        start, end = (j, q) if j < q else (k, r)
        tmp[i:] = nums[start:end]
        nums[p:r] = tmp[:]
    merge_sort_c(nums, 0, len(nums))

# 稳定非原地
def quick_sort0(nums: list):
    def partition(nums: list, p: int, r: int):
        pivot = nums[r-1]
        tmp_first = []
        tmp_second = []
        tmp_equal = []
        for i in range(p, r):
            if nums[i] < pivot:
                tmp_first.append(nums[i])
            elif nums[i] == pivot:
                tmp_equal.append(nums[i])
            else:
                tmp_second.append(nums[i])
        tmp_first.extend(tmp_equal)
        tmp_first.extend(tmp_second)
        nums[p: r] = tmp_first
        pivot_index = nums.index(pivot)
        return pivot_index
    def quick_sort_c(nums: list, p: int, r: int):
        if (r - p) > 1:
            q = partition(nums, p, r)
            quick_sort_c(nums, p, q)
            quick_sort_c(nums, q+1, r)
    quick_sort_c(nums, 0, len(nums))

# 非稳定原地
def quick_sort1(nums: list):
    def partition(nums: list, p: int, r: int):
        pivot_idx = random.randint(p, r-1)
        nums[pivot_idx], nums[r-1] = nums[r-1], nums[pivot_idx]
        i = p
        for j in range(p, r):
            if nums[j] <= nums[r-1]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return i - 1
    def quick_sort_c(nums: list, p: int, r: int):
        if (r - p) > 1:
            q = partition(nums, p, r)
            quick_sort_c(nums, p, q)
            quick_sort_c(nums, q+1, r)
    quick_sort_c(nums, 0, len(nums))

# 利用分治求无序数组中第 K 大元素
def k_max(nums: list, k: int):
    if k > len(nums) or k <=0:
        return None
    def partition(nums: List[int], start: int, end: int) -> int:
        pivot_idx = random.randint(start, end-1)
        nums[end-1], nums[pivot_idx] = nums[pivot_idx], nums[end-1]
        j = start
        for i in range(start, end):
            if nums[i] >= nums[end-1]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j - 1

    start, end = 0, len(nums)
    while True:
        mid = partition(nums, start, end)
        if k - 1 == mid:
            return nums[mid]
        elif k - 1 < mid:
            start = start
            end = mid
        else:
            start = mid+1
            end = end

# 桶排序
def bucket_sort(nums: list, m: int):
    # 找到最大值和最小值确定区间
    if not nums:
        return None
    if m < 1:
        raise ValueError('m should be greater than 1')
    maximum, minimum = nums[0], nums[0]
    for i in nums:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    interval = (maximum - minimum) / m
    buckets = [[] for _ in range(m)]
    # 分桶
    for i in nums:
        if i >= minimum and i < minimum + interval:
            buckets[0].append(i)
        elif i <= maximum and i >= (maximum - interval):
            buckets[-1].append(i)
        else:
            for j in range(1, m):
                if i >= j * interval and i < (j + 1) * interval:
                    buckets[j].append(i)
                    break
    # 合并每个桶
    k = 0
    for bucket in buckets:
        length = len(bucket)
        quick_sort1(bucket)
        nums[k: k+length] = bucket
        k += length
    return nums
                
if __name__ == "__main__":
    a = [2, 8, 1, 0, 1, 7, 20]
    # import time
    # start = time.clock()
    # merge_sort1(a)
    # end = time.clock()
    # print(end - start)
    # print(a[:5])
    merge_sort1(a)
    print(a)