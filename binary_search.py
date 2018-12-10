# @Time    : 2018/12/8 21:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# 有序数组不存在重复元素
def binary_search0_loop(nums: list, a):
    """
    :param nums: 有序列表
    :param a: 待查找元素
    :return: 元素在列表中的索引
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] == a:
            return mid
        elif nums[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    return None

def binary_search0_recursion(nums: list, a):
    def recursion(nums: list, low: int, high: int, a):
        if low > high:
            return None
        mid = low + ((high - low) >> 1)
        if nums[mid] == a:
            return mid
        elif nums[mid] < a:
            return recursion(nums, low=mid+1, high=high, a=a)
        else:
            return recursion(nums, low=low, high=mid-1, a=a)
    low, high = 0, len(nums) - 1
    return recursion(nums, low, high, a)


# 有序数组存在重复元素查找第一个匹配的元素
def binary_search1_loop(nums: list, a):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            high = mid - 1
        elif nums[mid] < a:
            low = mid + 1
        else:
            if nums[mid-1] != a or mid == 0:
                return mid
            else:
                high = mid - 1
    return None

def binary_search1_recursion(nums: list, a):
    def recursion(nums: list, low: int, high: int, a):
        if low > high:
            return None
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            return recursion(nums, low=low, high=mid-1, a=a)
        elif nums[mid] < a:
            return recursion(nums, low=mid+1, high=high, a=a)
        else:
            if nums[mid-1] != a or mid == 0:
                return mid
            else:
                return recursion(nums, low=low, high=mid-1, a=a)
    low, high = 0, len(nums)
    return recursion(nums, low, high, a)

# 有序数组存在重复元素查找最后一个匹配的元素
def binary_search2_loop(nums: list, a):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            high = mid - 1
        elif nums[mid] < a:
            low = mid + 1
        else:
            if nums[mid+1] != a or mid == (len(nums) - 1):
                return mid
            else:
                low = mid + 1
    return None

def binary_search2_recursion(nums: list, a):
    def recursion(nums: list, low: int, high: int, a):
        if low > high:
            return None
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            return recursion(nums, low=low, high=mid-1, a=a)
        elif nums[mid] < a:
            return recursion(nums, low=mid+1, high=high, a=a)
        else:
            if nums[mid+1] != a or mid == (len(nums) - 1):
                return mid
            else:
                return recursion(nums, low=mid+1, high=high, a=a)
    low, high = 0, len(nums)
    return recursion(nums, low, high, a)

# 有序数组中查找第一个大于等于给定值的元素
def binary_search3_loop(nums: list, a):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < a:
            low = mid + 1
        else:
            if nums[mid-1] < a or mid == 0:
                return mid
            else:
                high = mid - 1
    return None

def binary_search3_recursion(nums: list, a):
    def recursion(nums: list, low: int, high: int, a):
        if low > high:
            return None
        mid = low + ((high - low) >> 1)
        if nums[mid] < a:
            return recursion(nums, low=mid+1, high=high, a=a)
        else:
            if nums[mid-1] < a or mid == 0:
                return mid
            else:
                return recursion(nums, low=low, high=mid-1, a=a)
    low, high = 0, len(nums) - 1
    return recursion(nums, low, high, a)

# 有序数组中查找最后一个小于等于给定值的元素
def binary_search4_loop(nums: list, a):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            high = mid - 1
        else:
            if mid == (len(nums) - 1) or nums[mid+1] > a:
                return mid
            else:
                low = mid + 1
    return None

def binary_search4_recursion(nums: list, a):
    def recursion(nums, low: int, high: int, a):
        if low > high:
            return None
        mid = low + ((high - low) >> 1)
        if nums[mid] > a:
            return recursion(nums, low=low, high=mid-1, a=a)
        else:
            if mid == (len(nums) - 1) or nums[mid+1] > a:
                return mid
            else:
                return recursion(nums, low=mid+1, high=high, a=a)
    low, high = 0, len(nums) - 1
    return recursion(nums, low, high, a)

# 循环有序数组查找给定值元素
def binary_recycle_search0(nums: list, a):
    """
    找到分界下标
    """
    pivot = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            pivot = i
            break
    if nums[0] > a:
        low, high = pivot+1, len(nums)-1
    else:
        low, high = 0, pivot
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] == a:
            return mid
        elif nums[mid] > a:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    a = [4, 5, 6, 1, 2, 3]
    b = [4, 5, 6, 7, 1, 2, 3]
    c = [4, 6, 7, 1, 2, 3, 4]
    print(binary_recycle_search0(a, 0))