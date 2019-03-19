# @Time    : 2019/3/19 13:20
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

def lwst_bt(str1: str, str2: str):
    """
    回溯法求两字符串之间的莱温斯坦距离 (Levenshtein distance)
    """
    len1, len2 = len(str1), len(str2)
    min_dist = len1

    def back_tracking(i: int, j: int, dist: int):
        nonlocal min_dist
        if i == len1 or j == len2:
            if i < len1:
                dist += (len1 - i)
            if j < len2:
                dist += (len2 - j)
            if dist < min_dist:
                min_dist = dist
            return
        if str1[i] == str2[j]:
            back_tracking(i + 1, j + 1, dist)
        else:
            back_tracking(i + 1, j, dist + 1)
            back_tracking(i, j + 1, dist + 1)
            back_tracking(i + 1, j + 1, dist + 1)

    back_tracking(0, 0, 0)
    return min_dist


# def lwst_dynamic0(str1: str, str2: str):
#     length = len(str1)
#     states = [[0] * length for _ in range(length)]
#     # 初始化行
#     for j in range(length):
#         if str1[0] == str2[j]: states[0][j] = j
#
#         states[0][i] = states[0][i - 1] if str1[i - 1] == str2[0] else states[0][i - 1] + 1
#     # 初始化列
#     for j in range(1, length):
#         states[j][0] = states[j - 1][0] if str1[j - 1] == str2[0] else states[j - 1][0] + 1
#     for i in range(1, length):
#         for j in range(1, length):
#             cond1 = states[i - 1][j] + 1
#             cond2 = states[i][j - 1] + 1
#             cond3 = states[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else (states[i - 1][j - 1] + 1)
#             states[i][j] = min(cond1, cond2, cond3)
#     print(states)
#     return states[length - 1][length - 1]
#
#
# def lwst_dynamic1(str1: str, str2: str):
#     length = len(str1)
#     states = [[0] * length for _ in range(length)]
#
#     def recur(i, j):
#         if i == 0 or j == 0:
#             if i > 0:
#                 delta_dist = i if str1[i] == str2[0] else (i + 1)
#             elif j > 0:
#                 delta_dist = j if str2[j] == str1[0] else (j + 1)
#             else:
#                 delta_dist = 0 if str1[0] == str2[0] else 1
#             states[i][j] = delta_dist
#             return delta_dist
#         cond1 = recur(i - 1, j) + 1
#         cond2 = recur(i, j - 1) + 1
#         cond3 = recur(i - 1, j - 1) if str1[i] == str2[j] else (recur(i - 1, j - 1) + 1)
#         states[i][j] = min(cond1, cond2, cond3)
#         if i == length - 1 and j == length - 1: print(states)
#         return states[i][j]
#
#     return recur(length - 1, length - 1)


if __name__ == "__main__":
    # s1 = 'mitcmu'
    # s2 = 'mtacnu'
    s1 = 'ewquwq'
    s2 = 'erwewq'
    print(lwst_bt(s1, s2))
    # print(lwst_dynamic0(s1, s2))
    # print(lwst_dynamic1(s1, s2))
