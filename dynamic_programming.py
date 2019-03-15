# @Time    : 2019/3/15 13:55
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
对于一组不同重量、不可分割的物品，我们需要选择一些装入背包，在满足背包最大重量限制的前提下，
背包中物品总重量的最大值是多少呢
"""


# 时间复杂度 O(m*n), 空间复杂度 O(m*n)
def package01(items: list, w: int):
    items_num = len(items)
    states_num = w + 1
    # 初始化状态
    states = [[0] * states_num for _ in range(items_num)]
    states[0][items[0]] = 1
    states[0][0] = 1
    for i in range(1, items_num):
        # 装入第 i 个物品
        for j in range(w - items[i] + 1):
            if states[i - 1][j]:
                states[i][j + items[i]] = 1
        # 不装第 i 个物品
        for j in range(w + 1):
            if states[i - 1][j]:
                states[i][j] = 1
    for j in range(w, -1, -1):
        if states[items_num - 1][j]:
            return j
    return 0


# 优化空间消耗，时间复杂度不变，空间复杂度减小到 O(w+1)
def package01_opted(items: list, w: int):
    items_num = len(items)
    states_num = w + 1
    states = [0] * states_num
    states[0] = 1
    for i in range(items_num):
        for j in range(w - items[i], -1, -1):
            if states[j]:
                states[j + items[i]] = 1
    for k in range(w, -1, -1):
        if states[k]: return k
    return 0


"""
引入物品价值这一变量。对于一组不同重量、不同价值、不可分割的物品，我们选择将某些物品装入背包，在满足背包最大重量限制的前提下，
背包中可装入物品的总价值最大是多少呢？
"""


def super_package01(items: list, values: list, w: int):
    items_num = len(items)
    states_num = w + 1
    states = [[-1] * states_num for _ in range(items_num)]
    states[0][items[0]] = values[0]
    states[0][0] = 0
    for i in range(1, items_num):
        for j in range(w - items[i] + 1):
            if states[i - 1][j] >= 0:
                states[i][j + items[i]] = states[i - 1][j] + values[i]
        for j in range(w + 1):
            if states[i - 1][j] >= 0 and states[i - 1][j] > states[i][j]:
                states[i][j] = states[i - 1][j]

    max_val = -1
    for k in range(w, -1, -1):
        if states[items_num - 1][k] > max_val:
            max_val = states[items_num - 1][k]
    return max_val


def super1_package01(items: list, values: list, w: int):
    items_num = len(items)
    states_num = w + 1
    states = [[-1] * states_num for _ in range(items_num)]
    states[0][0] = 0
    states[0][items[0]] = values[0]
    for i in range(1, items_num):
        for j in range(w + 1):
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]
        for j in range(w - items[i] + 1):
            if states[i - 1][j] >= 0 and \
                    (states[i - 1][j] + values[i]) > states[i][j + items[i]]:
                states[i][j + items[i]] = states[i - 1][j] + values[i]
    max_val = -1
    for k in range(w, -1, -1):
        if states[items_num - 1][k] > max_val:
            max_val = states[items_num - 1][k]
    return max_val


def super_package01_opted(items: list, values: list, w: int):
    items_num = len(items)
    states_num = w + 1
    states = [-1] * states_num
    states[0] = 0
    for i in range(items_num):
        for j in range(w - items[i], -1, -1):
            if states[j] >= 0 and states[j] + values[i] > states[j + items[i]]:
                states[j + items[i]] = states[j] + values[i]
    max_val = -1
    for k in range(w, -1, -1):
        if states[k] > max_val:
            max_val = states[k]
    return max_val


if __name__ == "__main__":
    w = 9
    items = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    print(package01(items, w))
    print(package01_opted(items, w))
    print(super_package01(items, values, w))
    print(super1_package01(items, values, w))
    print(super_package01_opted(items, values, w))
