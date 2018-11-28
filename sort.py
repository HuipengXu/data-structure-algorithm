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
            q = p + (r - p) // 2
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
                i += 1
            else:
                tmp[i] = nums[k]
                k += 1
                i += 1
        start, end = (j, q) if j < q else (k, r)
        while start < end:
            tmp[i] = nums[start]
            start += 1
            i += 1
        nums[p: r] = tmp
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
        pivot = nums[r-1]
        i = p
        for j in range(p, r):
            if nums[j] <= pivot:
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
    def partition(nums: list, p: int, r: int):
        pivot = nums[r-1]
        i = p
        for j in range(p, r):
            if nums[j] >= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return i
    p = 0
    r = len(nums)
    while True:
        q = partition(nums, p, r)
        if q == k:
            return nums[q-1]
        elif q > k:
            p = 0
            r = q - 1
        else:
            p = q
            r = len(nums)
                
if __name__ == "__main__":
    # a = [i for i in range(9999, -1, -1)]
    # import time
    # start = time.clock()
    # merge_sort1(a)
    # end = time.clock()
    # print(end - start)
    # print(a[:5])
    test = [2, 4, 1, 5, 1, 9, 5, 0]
    print(k_max(test, 1))