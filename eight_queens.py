# @Time    : 2019/3/11 9:32
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


def cal_8queens(results: list, row: int):
    """
    results 下标表示所在行，存储的值表示列
    """
    if row == len(results):
        print_8queens(results)
        print('-----------------------')
        return
    for i in range(len(results)):
        if is_ok(results, row - 1, i):
            results[row] = i
            cal_8queens(results, row + 1)


def print_8queens(results):
    for k in range(len(results)):
        s = ''
        for m in range(len(results)):
            if results[k] == m:
                s += ' Q '
            else:
                s += ' * '
        print(s)


def is_ok(results, row, col):
    left_up = col - 1
    right_up = col + 1
    for i in range(row, -1, -1):
        if results[i] == col or results[i] == left_up or \
                results[i] == right_up:
            return False
        left_up -= 1
        right_up += 1
    return True


if __name__ == "__main__":
    results = [None] * 8
    cal_8queens(results, 0)
