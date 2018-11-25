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
    

            
                
if __name__ == "__main__":
    a = [i for i in range(9999, -1, -1)]
    import time
    start = time.clock()
    bubble_sort(a)
    end = time.clock()
    print(end - start)
    print(a[:5])
