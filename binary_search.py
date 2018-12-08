# @Time    : 2018/12/8 21:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# 有序数组不存在重复元素
def binary_search0(nums: list, a):
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

if __name__ == "__main__":
    a = [3, 2, 4, 1, 9, 5, 7]
    a.sort()
    print(a)
    print(binary_search0(a, 2))