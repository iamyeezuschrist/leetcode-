class Solution:
    def reverse(self, x: int) -> int:
        negative_sign = False
        if x < 0:
            negative_sign = True
            x = -x
        reversed = 0
        while x:
            reversed = (reversed * 10) + x % 10
            x = x // 10
        if reversed < 2147483647 and reversed >= -2147483648:
            return -reversed if negative_sign else reversed
        return 0
