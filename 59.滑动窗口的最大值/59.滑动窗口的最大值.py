# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        from Queue import deque
        queue = deque()
        res = []
        for i in range(len(num)):
            while(len(queue) and num[queue[-1]]<num[i]):   # 索引i对应值大的，要放在前面
                queue.pop()
            while(len(queue) and i - queue[0] + 1 > size):   # i - queue[0] + 1 这一步很关键
                queue.popleft()
            queue.append(i)
            if size and i - size  + 1>= 0:
                res.append(num[queue[0]])
        return res
