# @Time    : 2019/2/18 22:00
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

def brute_force(s: str, pat: str) -> bool:
    s_len, p_len = len(s), len(pat)
    for i in range(s_len - p_len + 1):
        count = 0
        for j in range(p_len):
            if pat[j] == s[i + j]:
                count += 1
        if count == p_len and \
                p_len != 0 and \
                s_len != 0: return True
    return False


def rabin_karp(s: str, pat: str) -> bool:
    s_len, p_len = len(s), len(pat)
    if p_len == 0: return False
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

    hash_vals = [hash_sub_str(s[:p_len])]
    for j in range(1, s_len - p_len + 1):
        next_hash = (hash_vals[j - 1] - pow_val[-1] * c2n[s[j - 1]]) * 26 + pow_val[0] * c2n[s[j + p_len - 1]]
        hash_vals.append(next_hash)
    pat_hash_val = hash_sub_str(pat)
    if pat_hash_val in hash_vals: return True
    return False


if __name__ == "__main__":
    s = 'ds'
    p = ''
    print(rabin_karp(s, p))
