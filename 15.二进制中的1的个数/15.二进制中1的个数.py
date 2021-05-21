# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
            # 则通过和一个32位的全1数字按位与运算
            # 可得到其补码二进制表示对应的十进制数（按位与运算把符号位的1视为了数字）
        while n:
            count += 1
            n = (n - 1) & n   # 将原 n 二进制中 最右边的 1 变为 0
        return count