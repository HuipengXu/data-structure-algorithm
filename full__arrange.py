# @Time    : 2019/3/11 16:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


def permutation(arr: list, m: int, n: int):
    if m == n:
        print_arrange(arr, n)
        return
    else:
        for i in range(m, len(arr)):
            arr[i], arr[m] = arr[m], arr[i]
            permutation(arr, m + 1, n)
            arr[i], arr[m] = arr[m], arr[i]


def print_arrange(arr, n):
    print(arr[:n])


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    permutation(arr, 0, 3)
