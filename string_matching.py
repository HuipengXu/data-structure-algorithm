# @Time    : 2019/2/18 22:00
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional, List, Tuple


def brute_force(s: str, pat: str) -> Optional[int]:
    s_len, p_len = len(s), len(pat)
    for i in range(s_len - p_len + 1):
        for j in range(p_len):
            if pat[j] != s[i + j]:
                break
            if j == p_len - 1:
                return i
    return None


def rabin_karp0(s: str, pat: str) -> Optional[int]:
    """
    将 a,b,....z 分别编号为 0,1,...25; 然后将子串表示为 26 进制数，进而转化成 10 进制数。
    显然，这个哈希过程是没有哈希冲突的, 但是当子串长度过大, 转换成 10 进制数将可能溢出
    """
    s_len, p_len = len(s), len(pat)
    if p_len == 0: return None
    a_idx = ord('a')
    c2n = {chr(c): c - a_idx for c in range(a_idx, a_idx + 26)}
    pow_val = [26 ** i for i in range(p_len)]

    def hash_sub_str(sub_str: str):
        hash_val = 0
        i = p_len - 1
        for c in sub_str:
            hash_val += pow_val[i] * c2n[c]
            i -= 1
        return hash_val

    pat_hash_val = hash_sub_str(pat)
    last = hash_sub_str(s[:p_len])
    for j in range(1, s_len - p_len + 1):
        if last == pat_hash_val: return j - 1
        last = (last - pow_val[-1] * c2n[s[j - 1]]) * 26 + pow_val[0] * c2n[s[j + p_len - 1]]
    if last == pat_hash_val: return s_len - p_len
    return None


def rabin_karp1(s: str, pat: str) -> Optional[int]:
    """
    将字母转换成 ascii 码，然后将字串中每个字母对应的 ascii 码，然后求和作为子串对应的哈希值，
    这种哈希方法很容易产生哈希冲突，解决办法是找到相同哈希值的子串后，再拿子串和模式串进行比对确认
    """
    s_len, p_len = len(s), len(pat)
    if p_len == 0: return None

    def hash_sub_str(sub_str: str):
        hash_val = 0
        for c in sub_str:
            hash_val += ord(c)
        return hash_val

    hash_vals = [hash_sub_str(s[:p_len])]
    for j in range(1, s_len - p_len + 1):
        next_hash = hash_vals[j - 1] - ord(s[j - 1]) + ord(s[j + p_len - 1])
        hash_vals.append(next_hash)
    pat_hash_val = hash_sub_str(pat)
    for idx in range(s_len - p_len + 1):
        if pat_hash_val == hash_vals[idx]:
            for m in range(p_len):
                if pat[m] != s[idx + m]:
                    break
                if m == p_len - 1:
                    return idx
    return None


def boyer_moore0(s: str, pat: str) -> Optional[int]:
    s_len, p_len = len(s), len(pat)
    i = p_len - 1
    while True:
        back = 0
        for j in range(p_len - 1, -1, -1):
            if pat[j] == s[i]:
                if j == 0:
                    return i
                i -= 1
                back += 1
            else:
                if (i + back) == s_len - 1: return None
                flag1 = flag2 = True
                move1 = move2 = 1
                # 坏字符规则
                while j >= 0:
                    if s[i] == pat[j]:
                        move1 = p_len - back - 1 - j
                        flag1 = False
                        break
                    j -= 1
                if flag1: move1 = p_len - back
                # 好后缀规则
                if back >= 1:
                    for m in range(p_len - 1, 0, -1):
                        if ((m - back) >= 0 and s[i + 1:i + back + 1] == pat[m - back:m]) \
                                or pat[:m] == s[i + back + 1 - m:i + back + 1]:
                            move2 = p_len - m
                            flag2 = False
                            break
                if flag2 and back >= 1: move2 = p_len
                # print('----------------------')
                # print('move1: %d' % move1)
                # print('move2: %d' % move2)
                # print('----------------------')
                move = max(move1, move2)
                i += (move + back)
                i = min(s_len - 1, i)
                break


def generate_bc(pat: str, p_len: int) -> list:
    bc = [-1] * 256
    for i in range(p_len):
        bc[ord(pat[i])] = i
    return bc


def generate_gs(pat: str, p_len: int) -> Tuple[list, list]:
    suffix = [-1] * p_len
    prefix = [False] * p_len
    for i in range(p_len - 1):
        k = 0
        j = i
        while j >= 0 and pat[p_len - 1 - k] == pat[j]:
            k += 1
            j -= 1
            suffix[k] = j + 1
        if j == -1: prefix[k] = True
    return suffix, prefix


def boyer_moore1(s: str, pat: str) -> Optional[int]:
    p_len, s_len = len(pat), len(s)
    bc = generate_bc(pat, p_len)
    suffix, prefix = generate_gs(pat, p_len)
    i = 0

    def move_by_gs(suffix: list, prefix: list, p_len: int, j: int):
        suffix_len = p_len - 1 - j
        if suffix[suffix_len] != -1:
            return j - suffix[suffix_len] + 1
        for m in range(j + 2, p_len):
            if prefix[p_len - m]:
                return m
        return p_len

    while i <= s_len - p_len:
        for j in range(p_len - 1, -1, -1):
            if pat[j] == s[i + j]:
                if j == 0: return i
                continue
            xi = bc[ord(s[i + j])]
            move1 = j - xi

            move2 = 1
            if j < p_len - 1:
                move2 = move_by_gs(suffix, prefix, p_len, j)
            move = max(move1, move2)
            # print('----------------------')
            # print('move1: %d' % move1)
            # print('move2: %d' % move2)
            # print('----------------------')
            i += move
            break
    return None


def kmp(s: str, pat: str):
    p_len, s_len = map(len, [pat, s])

    def get_nexts(pat: str, p_len: int):
        nexts = [-1] * (p_len - 1)
        for i in range(1, p_len - 1):
            k = nexts[i - 1] + 1
            if pat[k] == pat[i]:
                nexts[i] = k
                continue
            k -= 1
            flag = True
            while k >= 0:
                for j in range(1, k + 1):
                    if pat[k - j] != pat[i - j]:
                        flag = False
                        break
                if flag and pat[k] == pat[i]:
                    nexts[i] = k
                    break
                k -= 1
        return nexts

    nexts = get_nexts(pat, p_len)
    i = j = 0
    while j < p_len:
        if i >= s_len: return None
        if pat[j] == s[i]:
            i += 1
            j += 1
            continue
        k = nexts[j - 1] if j >= 1 else -1
        if k == -1 and j == 0: i += 1
        j = k + 1
    return i - p_len


if __name__ == "__main__":
    examples = [('sffsdgaaaaa', 'aa'), ('aaaaaaaaaa', 'baaa'), ('abcacabcbcbacabc', 'cbacabc'),
                ('sdfavfdcsfdfass', 'fdf'),
                ('abcacabcbcbacabc', 'abacabc'), ('fyjfjyhv', 'yhv'), ('aaaaaaaaaaaaa', 'aab'),
                ('ababaeabacababacd', 'ababacd')]
    for s, pat in examples:
        print(brute_force(s, pat))
        print(rabin_karp0(s, pat))
        print(rabin_karp1(s, pat))
        print(boyer_moore0(s, pat))
        # print('%%%%%%%%%%%%%%%%%')
        print(boyer_moore1(s, pat))
        print(kmp(s, pat))
        print('*******************')
