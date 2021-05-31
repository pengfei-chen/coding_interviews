# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        small = 1
        big = 2
        cur = 3
        while(small <= (tsum-1)//2):
            if cur == tsum:
                ans.append(list(range(small,big+1)))
                cur -= small
                small += 1
            elif cur > tsum:
                cur -= small
                small += 1
            else:
                big += 1
                cur += big
        return ans

# 参考答案
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        plow = 1
        phigh= 2
        while(phigh >  plow):
            cur = (phigh + plow) * (phigh - plow +1) / 2 # 等差数列求和 Sn=n(a1+an)/2
            if cur == tsum:
                List = []
                i = plow
                while i <= phigh:
                    List.append(i)
                    i += 1
                result.append(List)
                plow += 1
            elif cur < tsum:
                phigh += 1
            else:
                plow += 1
        return result