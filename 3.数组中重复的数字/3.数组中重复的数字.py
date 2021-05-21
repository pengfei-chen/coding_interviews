# -*- coding:utf-8 -*-
"""class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i, val in enumerate(numbers):
            if i!=val:
                if numbers[numbers[i]]==val:
                    duplication[0] = val
                    return True
                numbers[i] = numbers[val]
                numbers[val] = val
        return False"""

"""python中，for循环不能改变其中 i 的值。
调通的python版本代码如下。"""

class Solution:
    def duplicate(self , numbers ):
        # write code here
        i = 0
        length = len(numbers)
        while i < length:
            if numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                temp = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = temp
                i -= 1
            i += 1
        return -1

