# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) <5:
            return False
        d = [0]*14
        MAX = -1
        MIN = 14
        for i in range(len(numbers)):
            d[numbers[i]] += 1
            if numbers[i] == 0:
                continue
            if d[numbers[i]] > 1:   # 重复出现
                return False
            MAX = max(MAX,numbers[i])   # 记录当前最大值
            MIN = min(MIN,numbers[i])   # 记录当前最小值
        if MAX - MIN < 5:
            return True
        else:
            return False
        