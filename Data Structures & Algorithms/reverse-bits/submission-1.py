class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # extract ith bit of n
            res += (bit << (31 - i)) # shift this bit to position (31-i)
                                     # and add it to res
        return res