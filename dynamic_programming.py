# @Time    : 2019/3/15 13:55
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import sys

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


# 薅羊毛
def gathering_wool(values: list, full_redu_amt: int):
    """
    :param values: 所选所有商品的价格
    :param full_redu_amt: 满减金额
    :return: 达到满减要求的最低消费金额

    说明：无法找出具体要买的是哪些商品
    """
    states = [0] * sum(values)
    states[0] = 1
    min_amt = sum(values)
    for i in range(len(values)):
        for j in range(full_redu_amt - 1, -1, -1):
            if states[j]:
                amt = j + values[i]
                if amt >= full_redu_amt and amt < min_amt:
                    min_amt = amt
                states[amt] = 1
    return min_amt


def super_gathering_wool(values: list, full_redu_amt: int):
    items_num = len(values)
    states_num = sum(values) + 1
    states = [[0] * states_num for _ in range(items_num)]
    states[0][0] = 1
    states[0][values[0]] = 1
    for i in range(1, items_num):
        for j in range(states_num):
            if states[i - 1][j]:
                # 不买
                states[i][j] = 1
                # 买
                states[i][j + values[i]] = 1
    min_amt = states_num
    for k in range(full_redu_amt, states_num):
        if states[items_num - 1][k]:
            min_amt = k
            break
    purchased = []

    # 回溯拿到所有购买选项
    def get_purchase_options(amt: int, item: int):
        if item == 0:
            if amt != 0 and values[0] == amt:
                purchased.append(values[0])
                print(purchased)
                purchased.pop()
                return
            print(purchased)
            return
        if states[item - 1][amt]:
            get_purchase_options(amt, item - 1)
        if states[item - 1][amt - values[item]]:
            purchased.append(values[item])
            get_purchase_options(amt - values[item], item - 1)
            purchased.pop()

    get_purchase_options(min_amt, items_num - 1)
    return min_amt


# 杨辉三角
# 递推
def yh_triangle(triangle: list):
    height, width = len(triangle), len(triangle[0])
    states = [[sys.maxsize] * width for _ in range(height)]
    start = [idx for idx in range(width) if triangle[0][idx] != None][0]
    states[0][start] = triangle[0][start]
    for i in range(1, height):
        for j in range(width):
            if triangle[i][j] != None:
                left_up = states[i - 1][j - 1] if j - 1 >= 0 else sys.maxsize
                right_up = states[i - 1][j + 1] if j + 1 < width else sys.maxsize
                states[i][j] = triangle[i][j] + min(left_up, right_up)
    min_dist = sys.maxsize
    for k in range(width):
        if states[height - 1][k] < min_dist:
            min_dist = states[height - 1][k]
    return min_dist


# 递归
def yh_triangle_recur(triangle: list):
    height, width = len(triangle), len(triangle[0])
    states = [[sys.maxsize] * width for _ in range(height)]

    def min_dist(i, j):
        if j < 0 or j >= width or triangle[i][j] is None: return sys.maxsize
        if i == 0 and j == (width // 2): return triangle[0][width // 2]
        if states[i][j] != sys.maxsize: return states[i][j]

        left_up = min_dist(i - 1, j - 1)
        right_up = min_dist(i - 1, j + 1)

        states[i][j] = triangle[i][j] + min(left_up, right_up)

        return states[i][j]

    for j in range(width):
        if triangle[height - 1][j] != None:
            min_dist(height - 1, j)

    min_dis = states[height - 1][0]
    for k in range(1, width):
        if states[height - 1][k] < min_dis:
            min_dis = states[height - 1][k]
    return min_dis


if __name__ == "__main__":
    # w = 9
    # items = [2, 2, 4, 6, 3]
    # values = [3, 4, 8, 9, 6]
    # print(package01(items, w))
    # print(package01_opted(items, w))
    # print(super_package01(items, values, w))
    # print(super1_package01(items, values, w))
    # print(super_package01_opted(items, values, w))
    # values = [99, 59, 69, 89, 79, 39, 20]
    # full_redu_amt = 200
    # print(gathering_wool(values, full_redu_amt))
    # print(super_gathering_wool(values, full_redu_amt))
    yh = [[None, None, None, None, 5, None, None, None, None],
          [None, None, None, 7, None, 8, None, None, None],
          [None, None, 2, None, 3, None, 4, None, None, None],
          [None, 4, None, 9, None, 6, None, 1, None],
          [2, None, 7, None, 9, None, 4, None, 5]]
    print(yh_triangle(yh))
    print(yh_triangle_recur(yh))
