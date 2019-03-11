# @Time    : 2019/3/11 13:38
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

max_weight = 0


def package(i: int, cw: int, items: list, n: int, w: float):
    """
    :param i: 考察到第几个物品了
    :param cw: 目前背包中装了多重的物品
    :param items: 各个物品的重量
    :param n: 物品的总个数
    :param w: 背包的承重
    :return: 可装进物品的最大总重量
    """
    global max_weight
    if i == n or cw == w:
        if cw > max_weight:
            max_weight = cw
        return
    package(i + 1, cw, items, n, w)
    if cw + items[i] <= w:
        package(i + 1, cw + items[i], items, n, w)


if __name__ == "__main__":
    items = [9, 5, 7, 1]
    n = 4
    w = 20
    package(0, 0, items, n, w)
    print(max_weight)
