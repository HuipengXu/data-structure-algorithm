# @Time    : 2019/2/13 10:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
题目来源：https://time.geekbang.org/column/article/69388
"""


def cell_division(t: int) -> int:
    if t == 0:
        return 1
    elif t == 1:
        return 2
    elif t == 2:
        return 4
    elif t == 3:
        return 7
    else:
        return 2 * cell_division(t - 1) - cell_division(t - 4)


if __name__ == "__main__":
    print(cell_division(5))
