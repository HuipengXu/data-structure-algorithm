# @Time    : 2019/3/2 9:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

def merge_count(nums: list):
    inverse_degree = 0

    def partition(nums: list, low: int, high: int):
        if high - low == 1: return
        medium = low + ((high - low) >> 1)
        partition(nums, low, medium)
        partition(nums, medium, high)
        merge(nums, low, medium, high)

    def merge(nums: list, low: int, medium: int, high: int):
        nonlocal inverse_degree
        i, j, k = low, medium, 0
        temp = [0] * (high - low)
        while i < medium and j < high:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
                k += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1
                inverse_degree += 1
        if i == medium:
            while j < high:
                temp[k] = nums[j]
                j += 1
                k += 1
        elif j == high:
            inverse_degree += (medium - i - 1) * (high - medium)
            while i < medium:
                temp[k] = nums[i]
                i += 1
                k += 1
        m = 0
        while m < len(temp):
            nums[low + m] = temp[m]
            m += 1

    partition(nums, 0, len(nums))
    return inverse_degree


if __name__ == "__main__":
    a = [6, 5, 4, 3, 2, 1]
    print(merge_count(a))
