# @Time    : 2019/3/21 17:19
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class BitMap:

    def __init__(self, n_bits: int):
        self.n_bits = n_bits
        self._bytes = bytearray(n_bits // 8 + 1)

    def set(self, k: int):
        if k > self.n_bits or k < 0: return
        self._bytes[k // 8] |= (1 << k % 8)

    def get(self, k: int) -> bool:
        if k > self.n_bits or k < 0: return False
        return (self._bytes[k // 8] & (1 << k % 8)) != 0


if __name__ == '__main__':
    bm = BitMap(80)
    bm.set(80)
    print(bm.get(80))
